from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Copy_to_notebookPostRequest(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	groupId: Optional[str] = Field(default=None,alias="groupId",)
	renameAs: Optional[str] = Field(default=None,alias="renameAs",)
	siteCollectionId: Optional[str] = Field(default=None,alias="siteCollectionId",)
	siteId: Optional[str] = Field(default=None,alias="siteId",)


