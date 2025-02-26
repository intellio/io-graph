from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ListInfo(BaseModel):
	contentTypesEnabled: Optional[bool] = Field(default=None,alias="contentTypesEnabled",)
	hidden: Optional[bool] = Field(default=None,alias="hidden",)
	template: Optional[str] = Field(default=None,alias="template",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


