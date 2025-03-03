from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class FolderView(BaseModel):
	sortBy: Optional[str] = Field(default=None,alias="sortBy",)
	sortOrder: Optional[str] = Field(default=None,alias="sortOrder",)
	viewType: Optional[str] = Field(default=None,alias="viewType",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


