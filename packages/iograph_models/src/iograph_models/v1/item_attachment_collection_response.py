from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ItemAttachmentCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[ItemAttachment]] = Field(alias="value", default=None,)

from .item_attachment import ItemAttachment
