The main files are gradio_db_ui.py, openai_query.py and query_milvus.py

Steps to create the server (You need to be root in the following processes):
1. Install docker: https://docs.docker.com/engine/install/
2. Install milvus with docker: https://milvus.io/docs/install_standalone-docker.md

Before running the app insert the api keys to:
1. open ai api key to openai_query.py line 21. For openai api key, visit https://platform.openai.com/account/api-keys
2. cohere api key to query_milvus.py line 17. For cohere api key, visit https://dashboard.cohere.com/api-keys

Steps to create databases:
1. Insert your server's IP in the necessary fields of the scripts
2. Run all the cells in milvus_DB_creation_and_insertion.ipynb
3. Run all the cells in milvus_DB_creation_and_insertion.ipynb

To run with the UI:
    python3 gradio_db_ui.py
    
Gradio documentation: https://www.gradio.app/guides

To just see the query result in cohere db without UI:
1.  uncomment lines 54,55
2. python3 query_milvus.py

To just see the query result in openai db without UI:
1.  uncomment lines 54,55
2. python3 query_milvus.py

For more detailed information about the program, you can check the files in milvus_DB_notebooks folder.