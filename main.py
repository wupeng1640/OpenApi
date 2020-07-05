#/usr/bin/python
#coding:utf-8
# coding：utf-8
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello":"world"}

@app.get("/autotest/{item}")
def read_autp(item:int ,qq:str = "1645553538"):
    return {"item":item,'QQ':qq}

@app.get("/getbookinfo/")
def get_book_info(bookname:str='python book'):
    return {
        "bookname":bookname
    }

@app.post("/getbookinfodetail/")
def get_book_info_detail(bookname:str='python book'):
    return {
        "bookname":bookname
    }

