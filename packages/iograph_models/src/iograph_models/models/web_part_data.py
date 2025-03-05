from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WebPartData(BaseModel):
	dataVersion: Optional[str] = Field(default=None,alias="dataVersion",)
	description: Optional[str] = Field(default=None,alias="description",)
	properties: Optional[str] = Field(default=None,alias="properties",)
	serverProcessedContent: Optional[ServerProcessedContent] = Field(default=None,alias="serverProcessedContent",)
	title: Optional[str] = Field(default=None,alias="title",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .server_processed_content import ServerProcessedContent

