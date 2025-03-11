from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AndroidForWorkTrustedRootCertificateCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[AndroidForWorkTrustedRootCertificate]] = Field(alias="value",default=None,)

from .android_for_work_trusted_root_certificate import AndroidForWorkTrustedRootCertificate

