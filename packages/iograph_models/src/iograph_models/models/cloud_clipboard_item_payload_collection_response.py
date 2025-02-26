from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CloudClipboardItemPayloadCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[CloudClipboardItemPayload] = Field(alias="value",)

from .cloud_clipboard_item_payload import CloudClipboardItemPayload

