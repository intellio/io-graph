from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class LookupPostRequest(BaseModel):
	lookupValue: Optional[str] = Field(default=None,alias="lookupValue",)
	lookupVector: Optional[str] = Field(default=None,alias="lookupVector",)
	resultVector: Optional[str] = Field(default=None,alias="resultVector",)


