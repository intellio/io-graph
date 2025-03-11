from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ConvertPostRequest(BaseModel):
	number: Optional[str] = Field(alias="number",default=None,)
	fromUnit: Optional[str] = Field(alias="fromUnit",default=None,)
	toUnit: Optional[str] = Field(alias="toUnit",default=None,)


