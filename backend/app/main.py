from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class InterviewRequest ( BaseModel) :
    interview_type : str
    
    
 # api for home page   
@app.get("/")
def home():
    return {
        "message": "Welcome to AI Interview Coach "
    }

#api to start interview with type 
@app.post("/interview/start")
def start_interview(request:InterviewRequest):
     return{
        "message" : "Interview started",
        "interview_type" : request.interview_type
            
        }

# api to create questions

@app.get("/interview/question")
def get_question():
    return {
        "question " : "Tell me about yourself ?",
        "type" : "technical"
    }
    