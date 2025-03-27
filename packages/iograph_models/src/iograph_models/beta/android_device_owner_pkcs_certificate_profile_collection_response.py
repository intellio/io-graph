from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AndroidDeviceOwnerPkcsCertificateProfileCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[AndroidDeviceOwnerPkcsCertificateProfile]] = Field(alias="value", default=None,)

from .android_device_owner_pkcs_certificate_profile import AndroidDeviceOwnerPkcsCertificateProfile

