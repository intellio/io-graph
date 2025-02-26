from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Pkcs12CertificateInformation(BaseModel):
	isActive: Optional[bool] = Field(default=None,alias="isActive",)
	notAfter: Optional[int] = Field(default=None,alias="notAfter",)
	notBefore: Optional[int] = Field(default=None,alias="notBefore",)
	thumbprint: Optional[str] = Field(default=None,alias="thumbprint",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


