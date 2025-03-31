from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Image(BaseModel):
	height: Optional[int] = Field(alias="height", default=None,)
	width: Optional[int] = Field(alias="width", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

