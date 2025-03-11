from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DecimalPostRequest(BaseModel):
	number: Optional[str] = Field(alias="number",default=None,)
	radix: Optional[str] = Field(alias="radix",default=None,)


