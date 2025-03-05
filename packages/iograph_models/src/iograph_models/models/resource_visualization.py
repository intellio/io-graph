from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ResourceVisualization(BaseModel):
	containerDisplayName: Optional[str] = Field(default=None,alias="containerDisplayName",)
	containerType: Optional[str] = Field(default=None,alias="containerType",)
	containerWebUrl: Optional[str] = Field(default=None,alias="containerWebUrl",)
	mediaType: Optional[str] = Field(default=None,alias="mediaType",)
	previewImageUrl: Optional[str] = Field(default=None,alias="previewImageUrl",)
	previewText: Optional[str] = Field(default=None,alias="previewText",)
	title: Optional[str] = Field(default=None,alias="title",)
	type: Optional[str] = Field(default=None,alias="type",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


