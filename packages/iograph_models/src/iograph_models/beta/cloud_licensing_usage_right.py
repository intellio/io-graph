from __future__ import annotations
from uuid import UUID
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class CloudLicensingUsageRight(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.cloudLicensing.usageRight"] = Field(alias="@odata.type", default="#microsoft.graph.cloudLicensing.usageRight")
	services: Optional[list[CloudLicensingService]] = Field(alias="services", default=None,)
	skuId: Optional[UUID] = Field(alias="skuId", default=None,)
	skuPartNumber: Optional[str] = Field(alias="skuPartNumber", default=None,)

from .cloud_licensing_service import CloudLicensingService
