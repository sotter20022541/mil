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
    Name = Column(String,nullable=False)
    Surname = Column(String,nullable=False)
    Sex = Column(String,nullable=False)
    Year = Column(Integer)
    Dateofbirth = Column(String)
    Birthplace = Column(String)
    Nationality = Column(String)
    Education = Column(String)
    Relative = Column(String)
    PhoneforEmergency = Column(String)
    Phonestudent = Column(String)
    Address = Column(String)
    Email = Column(String)

class Disease(Base):
    __tablename__ = 'Disease'
    id_student = Column(Integer,primary_key=True)
    Disease = Column(String,primary_key=True)

class Activity(Base):
    __tablename__ = 'Activity'
    id_student = Column(Integer,primary_key=True)
    NameActivity = Column(String,primary_key=True)
    Description = Column(String)
    Photo = Column(String)#change next time
    Type = Column(String)
    Advisor = Column(String)
    Date_Activity = Column(String)
    File = Column(String)#change next time
    Confirm = Column(String)

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
    sum_all_credit = Column(Integer, nullable=False)
    GPAX = Column(String(5), nullable=True)

class Subject(Base):
    __tablename__ = 'subject'
    ID_Subject = Column(String(10),primary_key=True)
    name_subject = Column(String(50), nullable=False)
    Credit = Column(Integer, nullable=False)

Session = sessionmaker(bind=engine)
session = Session()
# Base.metadata.create_all(engine)
