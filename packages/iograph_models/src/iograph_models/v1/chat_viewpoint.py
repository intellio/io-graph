from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ChatViewpoint(BaseModel):
	isHidden: Optional[bool] = Field(alias="isHidden",default=None,)
	lastMessageReadDateTime: Optional[datetime] = Field(alias="lastMessageReadDateTime",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


