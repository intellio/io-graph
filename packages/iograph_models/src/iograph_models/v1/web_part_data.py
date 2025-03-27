from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WebPartData(BaseModel):
	dataVersion: Optional[str] = Field(alias="dataVersion", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	properties: Optional[str] = Field(alias="properties", default=None,)
	serverProcessedContent: Optional[ServerProcessedContent] = Field(alias="serverProcessedContent", default=None,)
	title: Optional[str] = Field(alias="title", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .server_processed_content import ServerProcessedContent

