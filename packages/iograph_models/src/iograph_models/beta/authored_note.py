from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AuthoredNote(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	author: SerializeAsAny[Optional[Identity]] = Field(alias="author",default=None,)
	content: Optional[ItemBody] = Field(alias="content",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)

from .identity import Identity
from .item_body import ItemBody

