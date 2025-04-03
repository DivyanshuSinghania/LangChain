from typing import List
from pydantic import BaseModel

class translateInput(BaseModel):
    
    fromlanguage: List[str]
    tolanguage: List[str]
    text: List[str]
    model: List[str]