from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class LookupPostRequest(BaseModel):
	lookupValue: Optional[str] = Field(alias="lookupValue", default=None,)
	lookupVector: Optional[str] = Field(alias="lookupVector", default=None,)
	resultVector: Optional[str] = Field(alias="resultVector", default=None,)


