from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class EnterpriseCodeSigningCertificate(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.enterpriseCodeSigningCertificate"] = Field(alias="@odata.type",)
	content: Optional[str] = Field(alias="content", default=None,)
	expirationDateTime: Optional[datetime] = Field(alias="expirationDateTime", default=None,)
	issuer: Optional[str] = Field(alias="issuer", default=None,)
	issuerName: Optional[str] = Field(alias="issuerName", default=None,)
	status: Optional[CertificateStatus | str] = Field(alias="status", default=None,)
	subject: Optional[str] = Field(alias="subject", default=None,)
	subjectName: Optional[str] = Field(alias="subjectName", default=None,)
	uploadDateTime: Optional[datetime] = Field(alias="uploadDateTime", default=None,)

from .certificate_status import CertificateStatus
