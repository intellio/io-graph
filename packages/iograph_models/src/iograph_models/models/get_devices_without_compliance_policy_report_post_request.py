from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Get_devices_without_compliance_policy_reportPostRequest(BaseModel):
	name: Optional[str] = Field(default=None,alias="name",)
	select: Optional[list[str]] = Field(default=None,alias="select",)
	groupBy: Optional[list[str]] = Field(default=None,alias="groupBy",)
	orderBy: Optional[list[str]] = Field(default=None,alias="orderBy",)
	search: Optional[str] = Field(default=None,alias="search",)
	skip: Optional[int] = Field(default=None,alias="skip",)
	top: Optional[int] = Field(default=None,alias="top",)
	sessionId: Optional[str] = Field(default=None,alias="sessionId",)
	filter: Optional[str] = Field(default=None,alias="filter",)


