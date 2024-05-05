from fastapi import FastAPI
from nicegui import app, ui
import aiohttp

async def test(num1, num2):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'http://localhost:8000/sum?num1={num1}&num2={num2}') as response:
            result = await response.json()
            return result['result']


async def compute_and_update_result(num1, num2):
    somma = await test(num1, num2)
    #ui.markdown(f'risultato : {somma}')
    ui.notify(f'risultato : {somma}')


def init(fastapi_app: FastAPI) -> None:
    @ui.page('/')
    async def home():
        ui.label('Hello, FastAPI! Pag1')

        # NOTE dark mode will be persistent for each user across tabs and server restarts
        ui.dark_mode().bind_value(app.storage.user, 'dark_mode')
        ui.checkbox('dark mode').bind_value(app.storage.user, 'dark_mode')
        ui.markdown('## Hello, ciuccelloni!')
        
        num1 = ui.number(label='Primo numero', value=5.6, format='%.2f',).bind_value(app.storage.user, 'num1')
        num2 = ui.number(label='Secondo numero', value=15.2, format='%.2f',).bind_value(app.storage.user, 'num2')
        #button = ui.button('risultato', on_click=lambda: ui.notify("IL RISULTATO DELLA SOMMA E'"+str(num1.value+num2.value)))  ## this works!
        button = ui.button('risultato', on_click=lambda: compute_and_update_result(num1.value, num2.value))


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