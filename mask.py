from transformers import pipeline
import gradio as gr
unmasker = pipeline('fill-mask', model = 'roberta-base')
interface = gr.Interface.from_pipeline(unmasker,
        title = "Fill Mask", examples = ["My <mask> is Alex.", "This website is <mask>!", "What are the requirements of this <mask>?"]).launch(share=True)

