from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class BitxorPostRequest(BaseModel):
	number1: Optional[str] = Field(default=None,alias="number1",)
	number2: Optional[str] = Field(default=None,alias="number2",)


