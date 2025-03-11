from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PermutPostRequest(BaseModel):
	number: Optional[str] = Field(alias="number",default=None,)
	numberChosen: Optional[str] = Field(alias="numberChosen",default=None,)


