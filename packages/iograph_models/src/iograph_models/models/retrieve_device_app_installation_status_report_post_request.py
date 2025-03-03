from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Retrieve_device_app_installation_status_reportPostRequest(BaseModel):
	name: Optional[str] = Field(default=None,alias="name",)
	select: Optional[list[str]] = Field(default=None,alias="select",)
	search: Optional[str] = Field(default=None,alias="search",)
	groupBy: Optional[list[str]] = Field(default=None,alias="groupBy",)
	orderBy: Optional[list[str]] = Field(default=None,alias="orderBy",)
	skip: Optional[int] = Field(default=None,alias="skip",)
	top: Optional[int] = Field(default=None,alias="top",)
	sessionId: Optional[str] = Field(default=None,alias="sessionId",)
	filter: Optional[str] = Field(default=None,alias="filter",)


