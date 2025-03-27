from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ActionItem(BaseModel):
	ownerDisplayName: Optional[str] = Field(alias="ownerDisplayName", default=None,)
	text: Optional[str] = Field(alias="text", default=None,)
	title: Optional[str] = Field(alias="title", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


