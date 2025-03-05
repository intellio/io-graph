from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class HlookupPostRequest(BaseModel):
	lookupValue: Optional[str] = Field(default=None,alias="lookupValue",)
	tableArray: Optional[str] = Field(default=None,alias="tableArray",)
	rowIndexNum: Optional[str] = Field(default=None,alias="rowIndexNum",)
	rangeLookup: Optional[str] = Field(default=None,alias="rangeLookup",)


