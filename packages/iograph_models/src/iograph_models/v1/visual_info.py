from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class VisualInfo(BaseModel):
	attribution: Optional[ImageInfo] = Field(alias="attribution", default=None,)
	backgroundColor: Optional[str] = Field(alias="backgroundColor", default=None,)
	content: Optional[str] = Field(alias="content", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayText: Optional[str] = Field(alias="displayText", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .image_info import ImageInfo

