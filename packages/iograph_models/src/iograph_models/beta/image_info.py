from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ImageInfo(BaseModel):
	addImageQuery: Optional[bool] = Field(alias="addImageQuery", default=None,)
	alternateText: Optional[str] = Field(alias="alternateText", default=None,)
	alternativeText: Optional[str] = Field(alias="alternativeText", default=None,)
	iconUrl: Optional[str] = Field(alias="iconUrl", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


