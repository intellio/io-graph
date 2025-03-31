from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class WhatIfApplicationContext(BaseModel):
	odata_type: Literal["#microsoft.graph.whatIfApplicationContext"] = Field(alias="@odata.type", default="#microsoft.graph.whatIfApplicationContext")
	includeApplications: Optional[list[str]] = Field(alias="includeApplications", default=None,)

