from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ServiceHealthIssuePost(BaseModel):
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	description: Optional[ItemBody] = Field(alias="description",default=None,)
	postType: Optional[str | PostType] = Field(alias="postType",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .item_body import ItemBody
from .post_type import PostType

