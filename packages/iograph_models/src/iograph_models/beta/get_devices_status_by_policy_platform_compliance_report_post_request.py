from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Get_devices_status_by_policy_platform_compliance_reportPostRequest(BaseModel):
	select: Optional[list[str]] = Field(alias="select", default=None,)
	groupBy: Optional[list[str]] = Field(alias="groupBy", default=None,)
	orderBy: Optional[list[str]] = Field(alias="orderBy", default=None,)
	search: Optional[str] = Field(alias="search", default=None,)
	skip: Optional[int] = Field(alias="skip", default=None,)
	top: Optional[int] = Field(alias="top", default=None,)
	sessionId: Optional[str] = Field(alias="sessionId", default=None,)
	filter: Optional[str] = Field(alias="filter", default=None,)

