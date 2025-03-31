from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MacOsVppAppAssignedLicenseCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[MacOsVppAppAssignedLicense]] = Field(alias="value", default=None,)

from .mac_os_vpp_app_assigned_license import MacOsVppAppAssignedLicense
