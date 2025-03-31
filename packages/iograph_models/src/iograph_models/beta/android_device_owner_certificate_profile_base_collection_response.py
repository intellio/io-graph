from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field


class AndroidDeviceOwnerCertificateProfileBaseCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[AndroidDeviceOwnerImportedPFXCertificateProfile, AndroidDeviceOwnerPkcsCertificateProfile, AndroidDeviceOwnerScepCertificateProfile],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .android_device_owner_imported_p_f_x_certificate_profile import AndroidDeviceOwnerImportedPFXCertificateProfile
from .android_device_owner_pkcs_certificate_profile import AndroidDeviceOwnerPkcsCertificateProfile
from .android_device_owner_scep_certificate_profile import AndroidDeviceOwnerScepCertificateProfile
