from pydantic import BaseModel, Field

class AccountCreate(BaseModel):
    account_type: str = Field(..., example="savings")
    initial_deposit: float = Field(..., example=1000.0)

class AccountResponse(BaseModel):
    account_number: str
    account_type: str
    initial_deposit: float

    class Config:
        orm_mode = True
