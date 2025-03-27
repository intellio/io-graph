from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MatchPostRequest(BaseModel):
	lookupValue: Optional[str] = Field(alias="lookupValue", default=None,)
	lookupArray: Optional[str] = Field(alias="lookupArray", default=None,)
	matchType: Optional[str] = Field(alias="matchType", default=None,)


