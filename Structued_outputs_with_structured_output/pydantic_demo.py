from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Student(BaseModel):

    # name:str

    #this is default value for name field if we don't pass any value for name field then it will take this default value.
    name:str = 'Alice'

    #None is set as default value for age field which means if we don't pass any value for age field then it will take None as default value.
    age:Optional[int]=None

    email:EmailStr='abc@gmail.com'

    #Field is used to add extra validation and metadata to the fields in the pydantic model. 
    # It allows us to specify constraints, default values, and descriptions for the fields.
    cgpa:float = Field(gt=5,lt=10,default=5.0,description='A decimal value representing the cgpa of the student')

new_student = {'name':'John'}
new_student_2 = {'name':'Bob','age':25}
#instead of john if i write 32 , error will be thrown because name field is expecting a string but we are passing an integer. 
# This is the power of pydantic it validates the data before creating the model instance.
#if i write 32 as '32' , pydantic will automatically convert it to integer because it is able to parse the string '32' as an integer. 
# This is called type coercion.

new_student_3 = {'name':'Bob','age':25,'email':'bob@example.com'}
#if i write bob.com or such error will throw because it has built in validation (EmailStr)

new_student_4 = {'name':'Bobby','age':25,'email':'boby@example.com','cgpa':9.5}


student=Student(**new_student)
student_2 = Student(**new_student_2)
student_3 = Student(**new_student_3)
student_4 = Student(**new_student_4)

# ** is called dictionary unpacking

# What it does
# Your dictionary:
# new_student = {'name': 'John'}

# Using ** converts it into:
# Student(name='John')
# Without ** (wrong way )
# Student(new_student)

# This will fail because:
# Pydantic expects named arguments


print(student)
#its output is name='John'

print(student_2)
print(student_3)
print(student_4)



student_dict = dict(student)

print(student_dict['age'])

student_json = student.model_dump_json()
print(student_json)