from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IfPostRequest(BaseModel):
	logicalTest: Optional[str] = Field(alias="logicalTest", default=None,)
	valueIfTrue: Optional[str] = Field(alias="valueIfTrue", default=None,)
	valueIfFalse: Optional[str] = Field(alias="valueIfFalse", default=None,)


