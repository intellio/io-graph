from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WhatIfApplicationContext(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	includeApplications: Optional[list[str]] = Field(alias="includeApplications",default=None,)


