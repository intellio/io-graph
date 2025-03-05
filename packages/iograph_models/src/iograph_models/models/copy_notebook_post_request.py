from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Copy_notebookPostRequest(BaseModel):
	groupId: Optional[str] = Field(default=None,alias="groupId",)
	renameAs: Optional[str] = Field(default=None,alias="renameAs",)
	notebookFolder: Optional[str] = Field(default=None,alias="notebookFolder",)
	siteCollectionId: Optional[str] = Field(default=None,alias="siteCollectionId",)
	siteId: Optional[str] = Field(default=None,alias="siteId",)


