from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SearchHit(BaseModel):
	contentSource: Optional[str] = Field(alias="contentSource",default=None,)
	hitId: Optional[str] = Field(alias="hitId",default=None,)
	isCollapsed: Optional[bool] = Field(alias="isCollapsed",default=None,)
	rank: Optional[int] = Field(alias="rank",default=None,)
	resultTemplateId: Optional[str] = Field(alias="resultTemplateId",default=None,)
	summary: Optional[str] = Field(alias="summary",default=None,)
	resource: SerializeAsAny[Optional[Entity]] = Field(alias="resource",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .entity import Entity

