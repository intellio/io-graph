from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Bundle(BaseModel):
	album: Optional[Album] = Field(alias="album", default=None,)
	childCount: Optional[int] = Field(alias="childCount", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .album import Album

