from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class EndpointPrivilegeManagementProvisioningStatus(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.endpointPrivilegeManagementProvisioningStatus"] = Field(alias="@odata.type",)
	licenseType: Optional[LicenseType | str] = Field(alias="licenseType", default=None,)
	onboardedToMicrosoftManagedPlatform: Optional[bool] = Field(alias="onboardedToMicrosoftManagedPlatform", default=None,)

from .license_type import LicenseType
