from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IosVppAppAssignedUserLicenseCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[IosVppAppAssignedUserLicense]] = Field(alias="value", default=None,)

from .ios_vpp_app_assigned_user_license import IosVppAppAssignedUserLicense

