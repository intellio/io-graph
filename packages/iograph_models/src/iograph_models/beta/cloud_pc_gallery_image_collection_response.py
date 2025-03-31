from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CloudPcGalleryImageCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[CloudPcGalleryImage]] = Field(alias="value", default=None,)

from .cloud_pc_gallery_image import CloudPcGalleryImage
