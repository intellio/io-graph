from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsCertificateProfileBaseCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[Windows10CertificateProfileBase, Windows10PkcsCertificateProfile, Windows10ImportedPFXCertificateProfile, Windows81CertificateProfileBase, Windows81SCEPCertificateProfile, WindowsPhone81ImportedPFXCertificateProfile]],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .windows10_certificate_profile_base import Windows10CertificateProfileBase
from .windows10_pkcs_certificate_profile import Windows10PkcsCertificateProfile
from .windows10_imported_p_f_x_certificate_profile import Windows10ImportedPFXCertificateProfile
from .windows81_certificate_profile_base import Windows81CertificateProfileBase
from .windows81_s_c_e_p_certificate_profile import Windows81SCEPCertificateProfile
from .windows_phone81_imported_p_f_x_certificate_profile import WindowsPhone81ImportedPFXCertificateProfile

