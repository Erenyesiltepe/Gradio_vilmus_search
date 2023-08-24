 
from pymilvus import connections, Collection
import openai  

def get_embedding(text, model="text-embedding-ada-002"):
   text = text.replace("\n", " ")
   return openai.Embedding.create(input = [text], model=model)['data'][0]['embedding']

def prepareDB():
    _HOST = ''#insert server ip here. If it is in local ip is 0.0.0.0
    _PORT = '19530'

    connections.connect(host=_HOST, port=_PORT, db_name="default")
    #print(db.list_database())
    
    collection = Collection("milvus_tr_embed")      # Get an existing collection.
    collection.load()
    return collection

def searchDB(query, collection=prepareDB()):
    openai.api_key="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" 
    query_embedding = get_embedding(query)
    
    search_params = {
        "metric_type": "IP", 
        "offset": 0, 
        "ignore_growing": False, 
        "params": {"nprobe": 10}
    }
    
    results = collection.search(
     data=[query_embedding], 
     anns_field="emb", 
     # the sum of `offset` in `param` and `limit` 
     # should be less than 16384.
     param=search_params,
     limit=5,
     expr=None,
     # set the names of the fields you want to 
     # retrieve from the search result.
     output_fields=["text"],
     consistency_level="Strong"
    )
    #print(results)
    data=""
    processed=results[0]
    for a in range(len(processed)):
        data+=(processed[a].entity.get("text")+"\n")
        data+=(str(processed[a].distance)+"\n\n")
        
    return data

#just to test
# result=searchDB("Atatürk?")
# print(result)
