from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class PartnersBillingManifest(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	blobCount: Optional[int] = Field(default=None,alias="blobCount",)
	blobs: list[PartnersBillingBlob] = Field(alias="blobs",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	dataFormat: Optional[str] = Field(default=None,alias="dataFormat",)
	eTag: Optional[str] = Field(default=None,alias="eTag",)
	partitionType: Optional[str] = Field(default=None,alias="partitionType",)
	partnerTenantId: Optional[str] = Field(default=None,alias="partnerTenantId",)
	rootDirectory: Optional[str] = Field(default=None,alias="rootDirectory",)
	sasToken: Optional[str] = Field(default=None,alias="sasToken",)
	schemaVersion: Optional[str] = Field(default=None,alias="schemaVersion",)

from .partners_billing_blob import PartnersBillingBlob

