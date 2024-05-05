import frontend
from fastapi import FastAPI
import uvicorn

app = FastAPI()

#####################################################################

@app.get('/home')
def read_root():
    return {'Hello': 'World'}


@app.get('/sum')
def somma(num1: float, num2: float):
    res = round(num1+num2, 2)
    print(res)
    return {'result': res}


#####################################################################
frontend.init(app)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)