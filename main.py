from fastapi import FastAPI, HTTPException, File, UploadFile, Header, Depends
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from scheamas import *
from envdata import load_env_data
from db_manager import DBManager


env_data = load_env_data()
database = DBManager(env_data)
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def start_page() -> str:
    return 'ฅ^•ﻌ•^ฅ Hello there!'

@app.get("/get_test")
async def get_test(invite_code : str):
    keys = ['test_id', 'name', 'invite_code', 'question_count']
    test = database.get_test(invite_code)
    if test:
        return {k:i for k,i in zip(keys,test)}
    else: 
        return {}

@app.get("/get_questions")
async def get_questions(test_id : int):
    keys = ['question_id', 'test_id', 'question_text', 'answer_one', 'answer_two','answer_three','answer_four','correct_answer']
    questions = database.get_questions(test_id)
    if questions:
        return {i:{k:i for k,i in zip(keys,questions[i])} for i in range(len(questions))}
    else: 
        return {}

@app.post("/add_user_result")
async def add_user_result(user_name : str, test_id : int, result : float):
    database.add_user_result(user_name, test_id, result)


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=3001)   