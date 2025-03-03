from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class CloudClipboardItem(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	expirationDateTime: Optional[datetime] = Field(default=None,alias="expirationDateTime",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	payloads: Optional[list[CloudClipboardItemPayload]] = Field(default=None,alias="payloads",)

from .cloud_clipboard_item_payload import CloudClipboardItemPayload

