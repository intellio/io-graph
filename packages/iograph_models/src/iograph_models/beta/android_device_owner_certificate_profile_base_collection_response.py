from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AndroidDeviceOwnerCertificateProfileBaseCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: SerializeAsAny[Optional[list[AndroidDeviceOwnerCertificateProfileBase]]] = Field(alias="value",default=None,)

from .android_device_owner_certificate_profile_base import AndroidDeviceOwnerCertificateProfileBase

