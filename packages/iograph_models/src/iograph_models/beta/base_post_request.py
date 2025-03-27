from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class BasePostRequest(BaseModel):
	number: Optional[str] = Field(alias="number", default=None,)
	radix: Optional[str] = Field(alias="radix", default=None,)
	minLength: Optional[str] = Field(alias="minLength", default=None,)


