from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class AndroidWorkProfileCertificateProfileBaseCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[AndroidWorkProfilePkcsCertificateProfile, AndroidWorkProfileScepCertificateProfile]],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .android_work_profile_pkcs_certificate_profile import AndroidWorkProfilePkcsCertificateProfile
from .android_work_profile_scep_certificate_profile import AndroidWorkProfileScepCertificateProfile

