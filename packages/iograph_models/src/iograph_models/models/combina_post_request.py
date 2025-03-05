from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CombinaPostRequest(BaseModel):
	number: Optional[str] = Field(default=None,alias="number",)
	numberChosen: Optional[str] = Field(default=None,alias="numberChosen",)


