from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class KeyLongValuePair(BaseModel):
	name: Optional[str] = Field(alias="name", default=None,)
	value: Optional[int] = Field(alias="value", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


