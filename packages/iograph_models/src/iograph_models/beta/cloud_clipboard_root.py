from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class CloudClipboardRoot(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.cloudClipboardRoot"] = Field(alias="@odata.type", default="#microsoft.graph.cloudClipboardRoot")
	items: Optional[list[CloudClipboardItem]] = Field(alias="items", default=None,)

from .cloud_clipboard_item import CloudClipboardItem
