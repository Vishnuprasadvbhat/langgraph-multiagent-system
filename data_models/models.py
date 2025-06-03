import re 
from pydantic import BaseModel, field_validator ,Field

class DateTimeModel(BaseModel):
  date:str= Field(description="Properly formated Date", pattern="*/d{2}-/d{2}-")