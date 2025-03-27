from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class ChatMessageHostedContent(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.chatMessageHostedContent"] = Field(alias="@odata.type", default="#microsoft.graph.chatMessageHostedContent")
	contentBytes: Optional[str] = Field(alias="contentBytes", default=None,)
	contentType: Optional[str] = Field(alias="contentType", default=None,)


