from sqlalchemy import Column, Integer, String
from .db import Base


class Completion(Base):
    __tablename__ = "completions"

    id = Column(String, primary_key=True, index=True, unique=True)
    object = Column(String)
    prompt = Column(String)
    model = Column(String)
    output = Column(String)
    prompt_cost = Column(Integer)
    output_cost = Column(Integer)
    total_cost = Column(Integer)
