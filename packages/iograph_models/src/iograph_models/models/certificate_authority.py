from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CertificateAuthority(BaseModel):
	certificate: Optional[str] = Field(default=None,alias="certificate",)
	certificateRevocationListUrl: Optional[str] = Field(default=None,alias="certificateRevocationListUrl",)
	deltaCertificateRevocationListUrl: Optional[str] = Field(default=None,alias="deltaCertificateRevocationListUrl",)
	isRootAuthority: Optional[bool] = Field(default=None,alias="isRootAuthority",)
	issuer: Optional[str] = Field(default=None,alias="issuer",)
	issuerSki: Optional[str] = Field(default=None,alias="issuerSki",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


