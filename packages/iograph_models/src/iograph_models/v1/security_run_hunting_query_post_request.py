from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Security_run_hunting_queryPostRequest(BaseModel):
	query: Optional[str] = Field(alias="query",default=None,)
	timespan: Optional[str] = Field(alias="timespan",default=None,)


