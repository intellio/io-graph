from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ManagementCertificateWithThumbprintCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[ManagementCertificateWithThumbprint]] = Field(alias="value",default=None,)

from .management_certificate_with_thumbprint import ManagementCertificateWithThumbprint

