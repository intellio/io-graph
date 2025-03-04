from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Get_recent_notebooks_with_includepersonalnotebooksGetResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[RecentNotebook]] = Field(default=None,alias="value",)

from .recent_notebook import RecentNotebook

