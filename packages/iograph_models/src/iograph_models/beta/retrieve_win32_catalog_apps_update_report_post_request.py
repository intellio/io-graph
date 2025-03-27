from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Retrieve_win32_catalog_apps_update_reportPostRequest(BaseModel):
	name: Optional[str] = Field(alias="name", default=None,)
	select: Optional[list[str]] = Field(alias="select", default=None,)
	search: Optional[str] = Field(alias="search", default=None,)
	groupBy: Optional[list[str]] = Field(alias="groupBy", default=None,)
	orderBy: Optional[list[str]] = Field(alias="orderBy", default=None,)
	skip: Optional[int] = Field(alias="skip", default=None,)
	top: Optional[int] = Field(alias="top", default=None,)
	sessionId: Optional[str] = Field(alias="sessionId", default=None,)
	filter: Optional[str] = Field(alias="filter", default=None,)


