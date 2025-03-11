from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IosVppAppAssignedLicenseCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: SerializeAsAny[Optional[list[IosVppAppAssignedLicense]]] = Field(alias="value",default=None,)

from .ios_vpp_app_assigned_license import IosVppAppAssignedLicense

