from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WindowsPhone81TrustedRootCertificateCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[WindowsPhone81TrustedRootCertificate]] = Field(alias="value", default=None,)

from .windows_phone81_trusted_root_certificate import WindowsPhone81TrustedRootCertificate
