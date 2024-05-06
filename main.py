import frontend
from fastapi import FastAPI, Depends
from pydantic import BaseModel
import uvicorn

app = FastAPI()

#####################################################################


class Inputdata(BaseModel):
    num1: float
    num2: float


@app.get('/home')
def read_root():
    return {'Hello': 'World'}


@app.get('/sum')
def somma_get(data: Inputdata = Depends()):
    res = round(data.num1+data.num2, 2)
    print(res)
    return {'result': res}


@app.post('/sum')
def somma_post(data: Inputdata = Depends):
    res = round(data.num1+data.num2, 2)
    print(res)
    return {'result': res}

#####################################################################


frontend.init(app)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)