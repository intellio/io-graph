from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class StringKeyLongValuePair(BaseModel):
	key: Optional[str] = Field(alias="key", default=None,)
	value: Optional[int] = Field(alias="value", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

