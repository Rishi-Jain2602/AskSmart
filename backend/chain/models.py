from pydantic import BaseModel

class UserQuery(BaseModel):
    user_id: str
    query: str
    # doctID:str