from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class RgbColor(BaseModel):
	b: Optional[int] = Field(alias="b", default=None,)
	g: Optional[int] = Field(alias="g", default=None,)
	r: Optional[int] = Field(alias="r", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

