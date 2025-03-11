from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AiInteractionAttachment(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	attachmentId: Optional[str] = Field(alias="attachmentId",default=None,)
	content: Optional[str] = Field(alias="content",default=None,)
	contentType: Optional[str] = Field(alias="contentType",default=None,)
	contentUrl: Optional[str] = Field(alias="contentUrl",default=None,)
	name: Optional[str] = Field(alias="name",default=None,)


