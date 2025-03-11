from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AndroidDeviceOwnerScepCertificateProfileCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[AndroidDeviceOwnerScepCertificateProfile]] = Field(alias="value",default=None,)

from .android_device_owner_scep_certificate_profile import AndroidDeviceOwnerScepCertificateProfile

