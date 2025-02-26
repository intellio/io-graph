from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SecuritySslCertificate(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	expirationDateTime: Optional[datetime] = Field(default=None,alias="expirationDateTime",)
	fingerprint: Optional[str] = Field(default=None,alias="fingerprint",)
	firstSeenDateTime: Optional[datetime] = Field(default=None,alias="firstSeenDateTime",)
	issueDateTime: Optional[datetime] = Field(default=None,alias="issueDateTime",)
	issuer: Optional[SecuritySslCertificateEntity] = Field(default=None,alias="issuer",)
	lastSeenDateTime: Optional[datetime] = Field(default=None,alias="lastSeenDateTime",)
	serialNumber: Optional[str] = Field(default=None,alias="serialNumber",)
	sha1: Optional[str] = Field(default=None,alias="sha1",)
	subject: Optional[SecuritySslCertificateEntity] = Field(default=None,alias="subject",)
	relatedHosts: list[SecurityHost] = Field(alias="relatedHosts",)

from .security_ssl_certificate_entity import SecuritySslCertificateEntity
from .security_ssl_certificate_entity import SecuritySslCertificateEntity
from .security_host import SecurityHost

