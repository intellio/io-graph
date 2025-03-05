from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RgbColor(BaseModel):
	b: Optional[int] = Field(default=None,alias="b",)
	g: Optional[int] = Field(default=None,alias="g",)
	r: Optional[int] = Field(default=None,alias="r",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


