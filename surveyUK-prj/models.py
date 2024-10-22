from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import column_property, sessionmaker
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import DateTime
from common.db import TblMixIn

DATABASE_NAME="newDB.sqlite"

engine= create_engine(f"sqlite:///{DATABASE_NAME}")
Session=sessionmaker(bind=engine)

Base= declarative_base()

def create_db():
    Base.metadata.create_all(engine)
    

class Human(Base,TblMixIn):
    __tablename__='humans'

    id=Column(Integer,primary_key=True)
    FIO=Column(String)
    email=Column(String)
    phone=Column(String)

    def __repr__(self):
        info:str = f'{self.FIO},{self.email},{self.phone},{self.id}'
        return info

class SurveyResults(Base,TblMixIn):
    __tablename__='survey_results'

    id=Column(Integer,primary_key=True)
    result=Column(String)
    datetime=Column(String)
    human_id=Column(Integer,ForeignKey('humans.id'))

    def __repr__(self):
        info:str = f'{self.result},{self.human_id},{self.datetime},{self.id}'
        return info

class QuestionsResults(Base,TblMixIn):
    __tablename__='questions_result'

    id=Column(Integer,primary_key=True)
    quest_number=Column(Integer)
    answer_number=Column(Integer)
    score=Column(Integer)
    flag=Column(String)
    result_id=Column(Integer,ForeignKey('survey_results.id'))

    def __repr__(self):
        info:str = f'{self.quest_number},{self.answer_number},{self.score},{self.flag},{self.result_id},{self.id}'
        return info