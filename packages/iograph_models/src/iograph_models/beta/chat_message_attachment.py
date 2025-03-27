from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ChatMessageAttachment(BaseModel):
	content: Optional[str] = Field(alias="content", default=None,)
	contentType: Optional[str] = Field(alias="contentType", default=None,)
	contentUrl: Optional[str] = Field(alias="contentUrl", default=None,)
	id: Optional[str] = Field(alias="id", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	teamsAppId: Optional[str] = Field(alias="teamsAppId", default=None,)
	thumbnailUrl: Optional[str] = Field(alias="thumbnailUrl", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


