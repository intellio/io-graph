from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Image(BaseModel):
	height: Optional[int] = Field(default=None,alias="height",)
	width: Optional[int] = Field(default=None,alias="width",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


