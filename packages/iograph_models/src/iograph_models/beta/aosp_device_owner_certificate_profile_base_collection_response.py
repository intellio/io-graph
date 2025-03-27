from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class AospDeviceOwnerCertificateProfileBaseCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[AospDeviceOwnerPkcsCertificateProfile, AospDeviceOwnerScepCertificateProfile],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .aosp_device_owner_pkcs_certificate_profile import AospDeviceOwnerPkcsCertificateProfile
from .aosp_device_owner_scep_certificate_profile import AospDeviceOwnerScepCertificateProfile

