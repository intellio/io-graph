from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class EnterpriseCodeSigningCertificate(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	content: Optional[str] = Field(default=None,alias="content",)
	expirationDateTime: Optional[datetime] = Field(default=None,alias="expirationDateTime",)
	issuer: Optional[str] = Field(default=None,alias="issuer",)
	issuerName: Optional[str] = Field(default=None,alias="issuerName",)
	status: Optional[CertificateStatus] = Field(default=None,alias="status",)
	subject: Optional[str] = Field(default=None,alias="subject",)
	subjectName: Optional[str] = Field(default=None,alias="subjectName",)
	uploadDateTime: Optional[datetime] = Field(default=None,alias="uploadDateTime",)

from .certificate_status import CertificateStatus

