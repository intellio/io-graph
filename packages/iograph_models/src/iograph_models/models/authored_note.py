from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class AuthoredNote(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	author: Optional[Identity] = Field(default=None,alias="author",)
	content: Optional[ItemBody] = Field(default=None,alias="content",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)

from .identity import Identity
from .item_body import ItemBody

