from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ChatMessageHostedContent(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	contentBytes: Optional[str] = Field(default=None,alias="contentBytes",)
	contentType: Optional[str] = Field(default=None,alias="contentType",)


