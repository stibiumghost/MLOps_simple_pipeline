import gradio as gr


def generate_image(text, mdjrny):
    # "mdjrny" to add prompthero/openjourney prompt
    if mdjrny:
        text += ', mdjrny-v4 style'
    return picture_gen(text)

if __name__ == '__main__':
    picture_gen = gr.Blocks.load(name='models/prompthero/openjourney')    # Stable Diffusion model for image generation

    with gr.Blocks() as image_generator:
        with gr.Row():

            with gr.Column(scale=1):
                pass

            with gr.Column(scale=2):
                gr.Markdown('## <p style="text-align: center;">IMAGE GENERATION</p>')
                my_image = gr.Image()
                seed = gr.Text(label='Input your prompt:')
                mdjrny = gr.Checkbox(label='In Openjourney style')
                btn = gr.Button('Generate image')
                gr.Examples(['Cold autumn morning', 'Lonely birthday party', 'Good day for muffins'], inputs=[seed])

            with gr.Column(scale=1):
                pass

        btn.click(generate_image, inputs=[seed, mdjrny], outputs=[my_image], api_name='api') #http://0.0.0.0:7860/run/api

    image_generator.launch(server_name='0.0.0.0')
