from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ResourceVisualization(BaseModel):
	containerDisplayName: Optional[str] = Field(alias="containerDisplayName",default=None,)
	containerType: Optional[str] = Field(alias="containerType",default=None,)
	containerWebUrl: Optional[str] = Field(alias="containerWebUrl",default=None,)
	mediaType: Optional[str] = Field(alias="mediaType",default=None,)
	previewImageUrl: Optional[str] = Field(alias="previewImageUrl",default=None,)
	previewText: Optional[str] = Field(alias="previewText",default=None,)
	title: Optional[str] = Field(alias="title",default=None,)
	type: Optional[str] = Field(alias="type",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


