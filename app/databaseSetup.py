import os
import sys
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///Database.db')
Base = declarative_base()

class Profile(Base):
    __tablename__ = 'Profile'
    id_student = Column(Integer,primary_key=True,nullable=False)
    Name = Column(String,nullable=True)
    Surname = Column(String,nullable=True)
    Sex = Column(String,nullable=True)
    Year = Column(Integer,nullable=True)
    Dateofbirth = Column(String,nullable=True)
    Birthplace = Column(String,nullable=True)
    Nationality = Column(String,nullable=True)
    Education = Column(String,nullable=True)
    Relative = Column(String,nullable=True)
    PhoneforEmergency = Column(String,nullable=True)
    Phonestudent = Column(String,nullable=True)
    Address = Column(String,nullable=True)
    Email = Column(String,nullable=True)
    Photo = Column(String,nullable=True)

class Disease(Base):
    __tablename__ = 'Disease'
    id_student = Column(Integer,primary_key=True)
    Disease = Column(String,primary_key=True)

class Activity(Base):
    __tablename__ = 'Activity'
    id_student = Column(Integer,primary_key=True)
    NameActivity = Column(String,primary_key=True)
    Description = Column(String,nullable=True)
    Photo = Column(String,nullable=True)#will be change next time
    Type = Column(String,nullable=True)
    Advisor = Column(String,nullable=True)
    Date_Activity = Column(String,nullable=True)
    File = Column(String,nullable=True)#will be change next time
    Confirm = Column(String,nullable=True)

class Academic(Base):
    __tablename__ = 'academic'
    Student_ID = Column(Integer,primary_key=True)
    Term = Column(String(6),primary_key=True)
    ID_Subject = Column(String(10),primary_key=True)
    Grade = Column(String(4), nullable=True)

class Gpa(Base):
    __tablename__ = 'gpa'
    Student_ID = Column(Integer,primary_key=True)
    Term = Column(String(6),primary_key=True)
    sum_credit = Column(Integer, nullable=True)
    GPA = Column(String(5), nullable=True)

class Gpax(Base):
    __tablename__ = 'gpax'
    Student_ID = Column(Integer,primary_key=True)
    sum_all_credit = Column(String(5), nullable=True)
    GPAX = Column(String(5), nullable=True)

class Subject(Base):
    __tablename__ = 'subject'
    ID_Subject = Column(String(10),primary_key=True)
    name_subject = Column(String(50), nullable=False)
    Credit = Column(Integer, nullable=True)

class TeacherPW(Base):
    __tablename__ = 'TeacherPW'
    id_teacher = Column(String,primary_key=True)
    Name = Column(String,nullable=True)
    Surname = Column(String,nullable=True)
    T_Password = Column(String,nullable=False)

class StudentPW(Base):
    __tablename__ = 'StudentPW'
    id_student = Column(String,primary_key=True,nullable=False)
    S_Password = Column(String,nullable=False)


Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)
