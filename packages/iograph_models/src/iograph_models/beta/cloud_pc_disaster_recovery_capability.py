from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CloudPcDisasterRecoveryCapability(BaseModel):
	capabilityType: Optional[CloudPcDisasterRecoveryCapabilityType | str] = Field(alias="capabilityType",default=None,)
	licenseType: Optional[CloudPcDisasterRecoveryLicenseType | str] = Field(alias="licenseType",default=None,)
	primaryRegion: Optional[str] = Field(alias="primaryRegion",default=None,)
	secondaryRegion: Optional[str] = Field(alias="secondaryRegion",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .cloud_pc_disaster_recovery_capability_type import CloudPcDisasterRecoveryCapabilityType
from .cloud_pc_disaster_recovery_license_type import CloudPcDisasterRecoveryLicenseType

