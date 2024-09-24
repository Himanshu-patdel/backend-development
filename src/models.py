from bunnet import Document
from pydantic import BaseModel

class Student(Document):
    name: str
    age: int
    grade: str

 
