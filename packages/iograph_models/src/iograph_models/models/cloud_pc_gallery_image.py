from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CloudPcGalleryImage(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	endDate: Optional[str] = Field(default=None,alias="endDate",)
	expirationDate: Optional[str] = Field(default=None,alias="expirationDate",)
	offerName: Optional[str] = Field(default=None,alias="offerName",)
	publisherName: Optional[str] = Field(default=None,alias="publisherName",)
	sizeInGB: Optional[int] = Field(default=None,alias="sizeInGB",)
	skuName: Optional[str] = Field(default=None,alias="skuName",)
	startDate: Optional[str] = Field(default=None,alias="startDate",)
	status: Optional[CloudPcGalleryImageStatus] = Field(default=None,alias="status",)

from .cloud_pc_gallery_image_status import CloudPcGalleryImageStatus

