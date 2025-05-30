from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class PartnersBillingManifest(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.partners.billing.manifest"] = Field(alias="@odata.type", default="#microsoft.graph.partners.billing.manifest")
	blobCount: Optional[int] = Field(alias="blobCount", default=None,)
	blobs: Optional[list[PartnersBillingBlob]] = Field(alias="blobs", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	dataFormat: Optional[str] = Field(alias="dataFormat", default=None,)
	eTag: Optional[str] = Field(alias="eTag", default=None,)
	partitionType: Optional[str] = Field(alias="partitionType", default=None,)
	partnerTenantId: Optional[str] = Field(alias="partnerTenantId", default=None,)
	rootDirectory: Optional[str] = Field(alias="rootDirectory", default=None,)
	sasToken: Optional[str] = Field(alias="sasToken", default=None,)
	schemaVersion: Optional[str] = Field(alias="schemaVersion", default=None,)

from .partners_billing_blob import PartnersBillingBlob
