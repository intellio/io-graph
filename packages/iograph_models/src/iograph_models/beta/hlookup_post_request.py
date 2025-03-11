from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class HlookupPostRequest(BaseModel):
	lookupValue: Optional[str] = Field(alias="lookupValue",default=None,)
	tableArray: Optional[str] = Field(alias="tableArray",default=None,)
	rowIndexNum: Optional[str] = Field(alias="rowIndexNum",default=None,)
	rangeLookup: Optional[str] = Field(alias="rangeLookup",default=None,)


