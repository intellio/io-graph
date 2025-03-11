from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsPhone81CertificateProfileBaseCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: SerializeAsAny[Optional[list[WindowsPhone81CertificateProfileBase]]] = Field(alias="value",default=None,)

from .windows_phone81_certificate_profile_base import WindowsPhone81CertificateProfileBase

