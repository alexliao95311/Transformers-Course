import gradio as gr
from transformers import pipeline
translator = pipeline('translation', model='Helsinki-NLP/opus-mt-en-zh')
interface = gr.Interface.from_pipeline(translator, title = 'English to Chinese Translator', examples = ["Hello!", "Good morning!", "What are you doing?"]).launch(share=True)
