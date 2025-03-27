from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Copy_notebookPostRequest(BaseModel):
	groupId: Optional[str] = Field(alias="groupId", default=None,)
	renameAs: Optional[str] = Field(alias="renameAs", default=None,)
	notebookFolder: Optional[str] = Field(alias="notebookFolder", default=None,)
	siteCollectionId: Optional[str] = Field(alias="siteCollectionId", default=None,)
	siteId: Optional[str] = Field(alias="siteId", default=None,)


