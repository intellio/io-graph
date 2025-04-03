from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class AiInteractionAttachment(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.aiInteractionAttachment"] = Field(alias="@odata.type", default="#microsoft.graph.aiInteractionAttachment")
	attachmentId: Optional[str] = Field(alias="attachmentId", default=None,)
	content: Optional[str] = Field(alias="content", default=None,)
	contentType: Optional[str] = Field(alias="contentType", default=None,)
	contentUrl: Optional[str] = Field(alias="contentUrl", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)

