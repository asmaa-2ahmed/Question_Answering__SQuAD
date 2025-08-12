from pydantic import BaseModel, Field, validator
from typing import Optional

class QARequest(BaseModel):
    """Request model for Question Answering"""
    context: str = Field(..., min_length=10, example="The Eiffel Tower is in Paris.")
    question: str = Field(..., min_length=3, example="Where is the Eiffel Tower?")

    @validator('context')
    def context_must_contain_letters(cls, v):
        if not any(c.isalpha() for c in v):
            raise ValueError("Context must contain meaningful text")
        return v

class QAResponse(BaseModel):
    """Response model for Question Answering"""
    answer: str
    score: float = Field(..., ge=0, le=1)
    start: int = Field(..., ge=0)
    end: int = Field(..., ge=0)
    context: Optional[str] = None
