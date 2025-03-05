from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CloudClipboardItemPayload(BaseModel):
	content: Optional[str] = Field(default=None,alias="content",)
	formatName: Optional[str] = Field(default=None,alias="formatName",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


