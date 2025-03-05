from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CertificateAuthority(BaseModel):
	certificate: Optional[str] = Field(alias="certificate",default=None,)
	certificateRevocationListUrl: Optional[str] = Field(alias="certificateRevocationListUrl",default=None,)
	deltaCertificateRevocationListUrl: Optional[str] = Field(alias="deltaCertificateRevocationListUrl",default=None,)
	isRootAuthority: Optional[bool] = Field(alias="isRootAuthority",default=None,)
	issuer: Optional[str] = Field(alias="issuer",default=None,)
	issuerSki: Optional[str] = Field(alias="issuerSki",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


