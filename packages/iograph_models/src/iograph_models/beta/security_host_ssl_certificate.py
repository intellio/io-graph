from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityHostSslCertificate(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	firstSeenDateTime: Optional[datetime] = Field(alias="firstSeenDateTime",default=None,)
	lastSeenDateTime: Optional[datetime] = Field(alias="lastSeenDateTime",default=None,)
	ports: Optional[list[SecurityHostSslCertificatePort]] = Field(alias="ports",default=None,)
	host: SerializeAsAny[Optional[SecurityHost]] = Field(alias="host",default=None,)
	sslCertificate: Optional[SecuritySslCertificate] = Field(alias="sslCertificate",default=None,)

from .security_host_ssl_certificate_port import SecurityHostSslCertificatePort
from .security_host import SecurityHost
from .security_ssl_certificate import SecuritySslCertificate

