from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CertificateAuthorityAsEntity(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	certificate: Optional[str] = Field(alias="certificate",default=None,)
	isRootAuthority: Optional[bool] = Field(alias="isRootAuthority",default=None,)
	issuer: Optional[str] = Field(alias="issuer",default=None,)
	issuerSubjectKeyIdentifier: Optional[str] = Field(alias="issuerSubjectKeyIdentifier",default=None,)


