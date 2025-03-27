from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ProfilePhoto(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	height: Optional[int] = Field(alias="height", default=None,)
	width: Optional[int] = Field(alias="width", default=None,)


