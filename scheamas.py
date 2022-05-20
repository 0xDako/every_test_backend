from pydantic import BaseModel

class Test(BaseModel):
    test_id : int = None
    name : str = None
    invite_code : str = None
    question_count : int = None

class User(BaseModel):
    user_id : int = None
    name : str = None
    test_id : str = None 
    result : float = None

class Question(BaseModel):
    question_id : int = None
    test_id : int = None
    question_text : str = None
    answer_one : str = None
    answer_two : str = None
    answer_three : str = None
    answer_four : str = None
    correct_answer : int = None