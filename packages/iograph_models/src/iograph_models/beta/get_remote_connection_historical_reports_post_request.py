from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Get_remote_connection_historical_reportsPostRequest(BaseModel):
	filter: Optional[str] = Field(alias="filter", default=None,)
	select: Optional[list[str]] = Field(alias="select", default=None,)
	search: Optional[str] = Field(alias="search", default=None,)
	groupBy: Optional[list[str]] = Field(alias="groupBy", default=None,)
	orderBy: Optional[list[str]] = Field(alias="orderBy", default=None,)
	skip: Optional[int] = Field(alias="skip", default=None,)
	top: Optional[int] = Field(alias="top", default=None,)


