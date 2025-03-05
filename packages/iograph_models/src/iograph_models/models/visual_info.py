from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class VisualInfo(BaseModel):
	attribution: Optional[ImageInfo] = Field(default=None,alias="attribution",)
	backgroundColor: Optional[str] = Field(default=None,alias="backgroundColor",)
	content: Optional[str] = Field(default=None,alias="content",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayText: Optional[str] = Field(default=None,alias="displayText",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .image_info import ImageInfo

