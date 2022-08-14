import gradio as gr
from transformers import pipeline
title = 'Question Answering App'
question_answerer = pipeline('question-answering', model = "deepset/roberta-base-squad2")
interface = gr.Interface.from_pipeline(question_answerer,
        title = title).launch(share=True)
