from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SearchHit(BaseModel):
	contentSource: Optional[str] = Field(default=None,alias="contentSource",)
	hitId: Optional[str] = Field(default=None,alias="hitId",)
	isCollapsed: Optional[bool] = Field(default=None,alias="isCollapsed",)
	rank: Optional[int] = Field(default=None,alias="rank",)
	resultTemplateId: Optional[str] = Field(default=None,alias="resultTemplateId",)
	summary: Optional[str] = Field(default=None,alias="summary",)
	resource: SerializeAsAny[Optional[Entity]] = Field(default=None,alias="resource",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .entity import Entity

