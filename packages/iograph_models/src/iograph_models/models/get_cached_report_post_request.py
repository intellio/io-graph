from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Get_cached_reportPostRequest(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	select: Optional[list[str]] = Field(default=None,alias="select",)
	groupBy: Optional[list[str]] = Field(default=None,alias="groupBy",)
	orderBy: Optional[list[str]] = Field(default=None,alias="orderBy",)
	search: Optional[str] = Field(default=None,alias="search",)
	skip: Optional[int] = Field(default=None,alias="skip",)
	top: Optional[int] = Field(default=None,alias="top",)


