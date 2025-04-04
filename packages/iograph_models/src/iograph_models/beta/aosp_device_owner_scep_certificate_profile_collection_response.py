from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AospDeviceOwnerScepCertificateProfileCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[AospDeviceOwnerScepCertificateProfile]] = Field(alias="value", default=None,)

from .aosp_device_owner_scep_certificate_profile import AospDeviceOwnerScepCertificateProfile
