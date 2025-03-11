from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AospDeviceOwnerCertificateProfileBaseCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: SerializeAsAny[Optional[list[AospDeviceOwnerCertificateProfileBase]]] = Field(alias="value",default=None,)

from .aosp_device_owner_certificate_profile_base import AospDeviceOwnerCertificateProfileBase

