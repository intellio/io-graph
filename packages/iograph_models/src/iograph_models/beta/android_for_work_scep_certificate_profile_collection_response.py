from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AndroidForWorkScepCertificateProfileCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[AndroidForWorkScepCertificateProfile]] = Field(alias="value",default=None,)

from .android_for_work_scep_certificate_profile import AndroidForWorkScepCertificateProfile

