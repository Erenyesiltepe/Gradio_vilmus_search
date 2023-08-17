import gradio as gr
import query_milvus as qm

#response function
def query_response(message, history):
    return qm.searchDB(message)

#main ui
demo = gr.ChatInterface(
    query_response,
    chatbot=gr.Chatbot(height=550),
    )

demo.launch(share="True")