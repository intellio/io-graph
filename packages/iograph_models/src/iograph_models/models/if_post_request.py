from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IfPostRequest(BaseModel):
	logicalTest: Optional[str] = Field(default=None,alias="logicalTest",)
	valueIfTrue: Optional[str] = Field(default=None,alias="valueIfTrue",)
	valueIfFalse: Optional[str] = Field(default=None,alias="valueIfFalse",)


