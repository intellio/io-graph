from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class ServiceHealthIssuePost(BaseModel):
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[ItemBody] = Field(default=None,alias="description",)
	postType: Optional[PostType] = Field(default=None,alias="postType",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .item_body import ItemBody
from .post_type import PostType

