from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ChatMessageAttachment(BaseModel):
	content: Optional[str] = Field(default=None,alias="content",)
	contentType: Optional[str] = Field(default=None,alias="contentType",)
	contentUrl: Optional[str] = Field(default=None,alias="contentUrl",)
	id: Optional[str] = Field(default=None,alias="id",)
	name: Optional[str] = Field(default=None,alias="name",)
	teamsAppId: Optional[str] = Field(default=None,alias="teamsAppId",)
	thumbnailUrl: Optional[str] = Field(default=None,alias="thumbnailUrl",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


