from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Bundle(BaseModel):
	album: Optional[Album] = Field(default=None,alias="album",)
	childCount: Optional[int] = Field(default=None,alias="childCount",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .album import Album

