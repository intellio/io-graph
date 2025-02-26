from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CloudClipboardRoot(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	items: list[CloudClipboardItem] = Field(alias="items",)

from .cloud_clipboard_item import CloudClipboardItem

