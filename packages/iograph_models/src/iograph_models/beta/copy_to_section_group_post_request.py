from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Copy_to_section_groupPostRequest(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	groupId: Optional[str] = Field(alias="groupId", default=None,)
	renameAs: Optional[str] = Field(alias="renameAs", default=None,)
	siteCollectionId: Optional[str] = Field(alias="siteCollectionId", default=None,)
	siteId: Optional[str] = Field(alias="siteId", default=None,)

