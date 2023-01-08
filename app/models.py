from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .db import Base


class Completion(Base):
    __tablename__ = "completions"

    id = Column(String, primary_key=True, index=True, unique=True)
    object = Column(String)
    prompt = Column(String)
    model = Column(String)
    output = Column(String)

    usage = relationship("Cost", back_populates="owner")


class Cost(Base):
    __tablename__ = "costs"

    id = Column(Integer, primary_key=True, index=True)
    prompt_cost = Column(Integer)
    output_cost = Column(Integer)
    total_cost = Column(Integer)
    completion_id = Column(String, ForeignKey("completions.id"))

    owner = relationship("Completion", back_populates="costs")
