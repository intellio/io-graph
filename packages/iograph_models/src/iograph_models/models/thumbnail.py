from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Thumbnail(BaseModel):
	content: Optional[str] = Field(default=None,alias="content",)
	height: Optional[int] = Field(default=None,alias="height",)
	sourceItemId: Optional[str] = Field(default=None,alias="sourceItemId",)
	url: Optional[str] = Field(default=None,alias="url",)
	width: Optional[int] = Field(default=None,alias="width",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


