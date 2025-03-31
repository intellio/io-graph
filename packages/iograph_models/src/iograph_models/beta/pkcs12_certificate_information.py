from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Pkcs12CertificateInformation(BaseModel):
	isActive: Optional[bool] = Field(alias="isActive", default=None,)
	notAfter: Optional[int] = Field(alias="notAfter", default=None,)
	notBefore: Optional[int] = Field(alias="notBefore", default=None,)
	thumbprint: Optional[str] = Field(alias="thumbprint", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

