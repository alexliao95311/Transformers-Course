from transformers import pipeline
import gradio as gr

classifier = pipeline('image-classification', model = 'google/vit-base-patch16-224')
interface = gr.Interface.from_pipeline(classifier,
        title = "Image Classifier").launch(share=True)

