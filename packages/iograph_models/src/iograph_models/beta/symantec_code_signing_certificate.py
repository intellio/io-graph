from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class SymantecCodeSigningCertificate(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.symantecCodeSigningCertificate"] = Field(alias="@odata.type", default="#microsoft.graph.symantecCodeSigningCertificate")
	content: Optional[str] = Field(alias="content", default=None,)
	expirationDateTime: Optional[datetime] = Field(alias="expirationDateTime", default=None,)
	issuer: Optional[str] = Field(alias="issuer", default=None,)
	issuerName: Optional[str] = Field(alias="issuerName", default=None,)
	password: Optional[str] = Field(alias="password", default=None,)
	status: Optional[CertificateStatus | str] = Field(alias="status", default=None,)
	subject: Optional[str] = Field(alias="subject", default=None,)
	subjectName: Optional[str] = Field(alias="subjectName", default=None,)
	uploadDateTime: Optional[datetime] = Field(alias="uploadDateTime", default=None,)

from .certificate_status import CertificateStatus
