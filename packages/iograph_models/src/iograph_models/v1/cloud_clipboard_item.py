from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class CloudClipboardItem(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.cloudClipboardItem"] = Field(alias="@odata.type", default="#microsoft.graph.cloudClipboardItem")
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	expirationDateTime: Optional[datetime] = Field(alias="expirationDateTime", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	payloads: Optional[list[CloudClipboardItemPayload]] = Field(alias="payloads", default=None,)

from .cloud_clipboard_item_payload import CloudClipboardItemPayload
