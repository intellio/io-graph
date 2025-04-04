from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AuthenticationSourceFilter(BaseModel):
	includeApplications: Optional[list[str]] = Field(alias="includeApplications", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

