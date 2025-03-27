from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class MacOSCertificateProfileBaseCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[MacOSImportedPFXCertificateProfile, MacOSPkcsCertificateProfile, MacOSScepCertificateProfile]],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .mac_o_s_imported_p_f_x_certificate_profile import MacOSImportedPFXCertificateProfile
from .mac_o_s_pkcs_certificate_profile import MacOSPkcsCertificateProfile
from .mac_o_s_scep_certificate_profile import MacOSScepCertificateProfile

