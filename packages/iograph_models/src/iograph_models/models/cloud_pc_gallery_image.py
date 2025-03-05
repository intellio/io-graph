from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CloudPcGalleryImage(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	endDate: Optional[str] = Field(alias="endDate",default=None,)
	expirationDate: Optional[str] = Field(alias="expirationDate",default=None,)
	offerName: Optional[str] = Field(alias="offerName",default=None,)
	publisherName: Optional[str] = Field(alias="publisherName",default=None,)
	sizeInGB: Optional[int] = Field(alias="sizeInGB",default=None,)
	skuName: Optional[str] = Field(alias="skuName",default=None,)
	startDate: Optional[str] = Field(alias="startDate",default=None,)
	status: Optional[str | CloudPcGalleryImageStatus] = Field(alias="status",default=None,)

from .cloud_pc_gallery_image_status import CloudPcGalleryImageStatus

