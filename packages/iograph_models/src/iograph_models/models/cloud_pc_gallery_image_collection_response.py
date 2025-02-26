from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CloudPcGalleryImageCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[CloudPcGalleryImage] = Field(alias="value",)

from .cloud_pc_gallery_image import CloudPcGalleryImage

