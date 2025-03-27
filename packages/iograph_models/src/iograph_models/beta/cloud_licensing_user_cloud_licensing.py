from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CloudLicensingUserCloudLicensing(BaseModel):
	usageRights: Optional[list[CloudLicensingUsageRight]] = Field(alias="usageRights", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .cloud_licensing_usage_right import CloudLicensingUsageRight

