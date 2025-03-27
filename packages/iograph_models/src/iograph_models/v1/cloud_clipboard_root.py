from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CloudClipboardRoot(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	items: Optional[list[CloudClipboardItem]] = Field(alias="items", default=None,)

from .cloud_clipboard_item import CloudClipboardItem

