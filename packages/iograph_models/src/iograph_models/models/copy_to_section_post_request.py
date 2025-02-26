from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Copy_to_sectionPostRequest(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	groupId: Optional[str] = Field(default=None,alias="groupId",)
	siteCollectionId: Optional[str] = Field(default=None,alias="siteCollectionId",)
	siteId: Optional[str] = Field(default=None,alias="siteId",)


