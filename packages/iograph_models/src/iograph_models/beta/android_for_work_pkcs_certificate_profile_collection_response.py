from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AndroidForWorkPkcsCertificateProfileCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[AndroidForWorkPkcsCertificateProfile]] = Field(alias="value", default=None,)

from .android_for_work_pkcs_certificate_profile import AndroidForWorkPkcsCertificateProfile
