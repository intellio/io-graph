from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class EndpointPrivilegeManagementProvisioningStatus(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	licenseType: Optional[LicenseType | str] = Field(alias="licenseType", default=None,)
	onboardedToMicrosoftManagedPlatform: Optional[bool] = Field(alias="onboardedToMicrosoftManagedPlatform", default=None,)

from .license_type import LicenseType

