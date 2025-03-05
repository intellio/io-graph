from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class VlookupPostRequest(BaseModel):
	lookupValue: Optional[str] = Field(default=None,alias="lookupValue",)
	tableArray: Optional[str] = Field(default=None,alias="tableArray",)
	colIndexNum: Optional[str] = Field(default=None,alias="colIndexNum",)
	rangeLookup: Optional[str] = Field(default=None,alias="rangeLookup",)


