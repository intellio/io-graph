from __future__ import annotations
from uuid import UUID
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CloudLicensingUsageRight(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	services: Optional[list[CloudLicensingService]] = Field(alias="services", default=None,)
	skuId: Optional[UUID] = Field(alias="skuId", default=None,)
	skuPartNumber: Optional[str] = Field(alias="skuPartNumber", default=None,)

from .cloud_licensing_service import CloudLicensingService

