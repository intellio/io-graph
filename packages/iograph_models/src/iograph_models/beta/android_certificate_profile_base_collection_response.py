from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class AndroidCertificateProfileBaseCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[AndroidForWorkImportedPFXCertificateProfile, AndroidImportedPFXCertificateProfile, AndroidPkcsCertificateProfile, AndroidScepCertificateProfile]],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .android_for_work_imported_p_f_x_certificate_profile import AndroidForWorkImportedPFXCertificateProfile
from .android_imported_p_f_x_certificate_profile import AndroidImportedPFXCertificateProfile
from .android_pkcs_certificate_profile import AndroidPkcsCertificateProfile
from .android_scep_certificate_profile import AndroidScepCertificateProfile

