from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TeamsTabConfiguration(BaseModel):
	contentUrl: Optional[str] = Field(default=None,alias="contentUrl",)
	entityId: Optional[str] = Field(default=None,alias="entityId",)
	removeUrl: Optional[str] = Field(default=None,alias="removeUrl",)
	websiteUrl: Optional[str] = Field(default=None,alias="websiteUrl",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


