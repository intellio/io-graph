from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AndroidForWorkCertificateProfileBaseCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: SerializeAsAny[Optional[list[AndroidForWorkCertificateProfileBase]]] = Field(alias="value",default=None,)

from .android_for_work_certificate_profile_base import AndroidForWorkCertificateProfileBase

