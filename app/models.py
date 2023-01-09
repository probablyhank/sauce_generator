from sqlalchemy import Column, Integer, String
from .db import Base

# shave down to one table shape- costs will be in completions table - DO NOT NEED RELATIONSHIP


class Completion(Base):
    __tablename__ = "completions"

    id = Column(String, primary_key=True, index=True, unique=True)
    object = Column(String)
    prompt = Column(String)
    model = Column(String)
    # consider making column this a JSON array for plurals
    output = Column(String)
    prompt_cost = Column(Integer)
    output_cost = Column(Integer)
    total_cost = Column(Integer)
