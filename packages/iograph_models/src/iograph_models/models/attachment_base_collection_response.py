from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AttachmentBaseCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[AttachmentBase] = Field(alias="value",)

from .attachment_base import AttachmentBase

