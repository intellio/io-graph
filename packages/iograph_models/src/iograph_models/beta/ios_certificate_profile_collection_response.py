from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class IosCertificateProfileCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[IosCertificateProfileBase, IosPkcsCertificateProfile, IosScepCertificateProfile, IosImportedPFXCertificateProfile],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .ios_certificate_profile_base import IosCertificateProfileBase
from .ios_pkcs_certificate_profile import IosPkcsCertificateProfile
from .ios_scep_certificate_profile import IosScepCertificateProfile
from .ios_imported_p_f_x_certificate_profile import IosImportedPFXCertificateProfile

