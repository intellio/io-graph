from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AndroidWorkProfileCertificateProfileBaseCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: SerializeAsAny[Optional[list[AndroidWorkProfileCertificateProfileBase]]] = Field(alias="value",default=None,)

from .android_work_profile_certificate_profile_base import AndroidWorkProfileCertificateProfileBase

