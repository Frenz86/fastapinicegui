from fastapi import FastAPI
from nicegui import app, ui
import aiohttp


async def apicall(num1, num2):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'http://localhost:8000/sum?num1={num1}&num2={num2}') as response:
            result = await response.json()
            return result['result']


def init(fastapi_app: FastAPI) -> None:
    @ui.page('/')
    async def home():
        ui.label('Hello, FastAPI! Pag1')
        # NOTE dark mode will be persistent for each user across tabs and server restarts
        ui.dark_mode().bind_value(app.storage.user, 'dark_mode')
        ui.checkbox('dark mode').bind_value(app.storage.user, 'dark_mode')
        ui.markdown('## Hello, ciuccelloni!')
        
        num1 = ui.number(label='Primo numero', value=5.6, format='%.2f',)
        num2 = ui.number(label='Secondo numero', value=15.2, format='%.2f',)

        async def handle_click():
            result = await apicall(num1.value, num2.value)
            ui.notify(f'risultato : {result}')
            markdown.content = f"#### result = {result}"

        ui.button('risultato', on_click=handle_click)
        markdown = ui.markdown()


    @ui.page('/pag2')
    async def page2():
        ui.label('Hello, FastAPI! Pag2')

        # NOTE dark mode will be persistent for each user across tabs and server restarts
        ui.dark_mode().bind_value(app.storage.user, 'dark_mode')
        ui.checkbox('dark mode').bind_value(app.storage.user, 'dark_mode')
        ui.markdown('## Hello, ciuccelloni!')
    # #################################################################################################

    ui.run_with(
                fastapi_app,
                mount_path='/',  # NOTE this can be omitted if you want the paths passed to @ui.page to be at the root
                storage_secret='pick your private secret here',  # NOTE setting a secret is optional but allows for persistent storage per user
                )