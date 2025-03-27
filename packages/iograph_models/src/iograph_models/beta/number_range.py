from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class NumberRange(BaseModel):
	lowerNumber: Optional[int] = Field(alias="lowerNumber", default=None,)
	upperNumber: Optional[int] = Field(alias="upperNumber", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


