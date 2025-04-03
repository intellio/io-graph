from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class CloudPcGalleryImage(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.cloudPcGalleryImage"] = Field(alias="@odata.type", default="#microsoft.graph.cloudPcGalleryImage")
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	endDate: Optional[str] = Field(alias="endDate", default=None,)
	expirationDate: Optional[str] = Field(alias="expirationDate", default=None,)
	offer: Optional[str] = Field(alias="offer", default=None,)
	offerDisplayName: Optional[str] = Field(alias="offerDisplayName", default=None,)
	offerName: Optional[str] = Field(alias="offerName", default=None,)
	osVersionNumber: Optional[str] = Field(alias="osVersionNumber", default=None,)
	publisher: Optional[str] = Field(alias="publisher", default=None,)
	publisherName: Optional[str] = Field(alias="publisherName", default=None,)
	recommendedSku: Optional[str] = Field(alias="recommendedSku", default=None,)
	sizeInGB: Optional[int] = Field(alias="sizeInGB", default=None,)
	sku: Optional[str] = Field(alias="sku", default=None,)
	skuDisplayName: Optional[str] = Field(alias="skuDisplayName", default=None,)
	skuName: Optional[str] = Field(alias="skuName", default=None,)
	startDate: Optional[str] = Field(alias="startDate", default=None,)
	status: Optional[CloudPcGalleryImageStatus | str] = Field(alias="status", default=None,)

from .cloud_pc_gallery_image_status import CloudPcGalleryImageStatus
