from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Get_device_non_compliance_reportPostRequest(BaseModel):
	name: Optional[str] = Field(default=None,alias="name",)
	select: list[Optional[str]] = Field(alias="select",)
	groupBy: list[Optional[str]] = Field(alias="groupBy",)
	orderBy: list[Optional[str]] = Field(alias="orderBy",)
	search: Optional[str] = Field(default=None,alias="search",)
	skip: Optional[int] = Field(default=None,alias="skip",)
	top: Optional[int] = Field(default=None,alias="top",)
	sessionId: Optional[str] = Field(default=None,alias="sessionId",)
	filter: Optional[str] = Field(default=None,alias="filter",)


