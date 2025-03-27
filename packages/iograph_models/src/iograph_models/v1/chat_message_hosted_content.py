from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ChatMessageHostedContent(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	contentBytes: Optional[str] = Field(alias="contentBytes", default=None,)
	contentType: Optional[str] = Field(alias="contentType", default=None,)


