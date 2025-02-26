from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PrintDocument(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	contentType: Optional[str] = Field(default=None,alias="contentType",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	size: Optional[int] = Field(default=None,alias="size",)


