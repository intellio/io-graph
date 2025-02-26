from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ImageInfo(BaseModel):
	addImageQuery: Optional[bool] = Field(default=None,alias="addImageQuery",)
	alternateText: Optional[str] = Field(default=None,alias="alternateText",)
	alternativeText: Optional[str] = Field(default=None,alias="alternativeText",)
	iconUrl: Optional[str] = Field(default=None,alias="iconUrl",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


