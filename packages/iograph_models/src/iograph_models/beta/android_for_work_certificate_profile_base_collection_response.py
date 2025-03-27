from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class AndroidForWorkCertificateProfileBaseCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[AndroidForWorkPkcsCertificateProfile, AndroidForWorkScepCertificateProfile]],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .android_for_work_pkcs_certificate_profile import AndroidForWorkPkcsCertificateProfile
from .android_for_work_scep_certificate_profile import AndroidForWorkScepCertificateProfile

