from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Security_run_hunting_queryPostRequest(BaseModel):
	query: Optional[str] = Field(default=None,alias="query",)
	timespan: Optional[str] = Field(default=None,alias="timespan",)


