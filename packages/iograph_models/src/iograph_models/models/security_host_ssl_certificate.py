from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityHostSslCertificate(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	firstSeenDateTime: Optional[datetime] = Field(default=None,alias="firstSeenDateTime",)
	lastSeenDateTime: Optional[datetime] = Field(default=None,alias="lastSeenDateTime",)
	ports: Optional[list[SecurityHostSslCertificatePort]] = Field(default=None,alias="ports",)
	host: Optional[SecurityHost] = Field(default=None,alias="host",)
	sslCertificate: Optional[SecuritySslCertificate] = Field(default=None,alias="sslCertificate",)

from .security_host_ssl_certificate_port import SecurityHostSslCertificatePort
from .security_host import SecurityHost
from .security_ssl_certificate import SecuritySslCertificate

