from pydantic import BaseModel

class StudentCreate(BaseModel):
    name: str
    age: int
    grade: str

class StudentResponse(BaseModel):
    id: str
    name: str
    age: int
    grade: str




# from pydantic import BaseModel

# class StudentBase(BaseModel):
#     name: str
#     age: int
#     grade: str

# class StudentCreate(StudentBase):
#     pass

# class StudentResponse(StudentBase):
#     id: str
