from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime

from database import Base


class Prompt(Base):
    __tablename__ = "prompts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    content = Column(Text, nullable=False)
    expected_result = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)