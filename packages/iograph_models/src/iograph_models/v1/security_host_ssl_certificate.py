from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityHostSslCertificate(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.security.hostSslCertificate"] = Field(alias="@odata.type", default="#microsoft.graph.security.hostSslCertificate")
	firstSeenDateTime: Optional[datetime] = Field(alias="firstSeenDateTime", default=None,)
	lastSeenDateTime: Optional[datetime] = Field(alias="lastSeenDateTime", default=None,)
	ports: Optional[list[SecurityHostSslCertificatePort]] = Field(alias="ports", default=None,)
	host: Optional[Union[SecurityHostname, SecurityIpAddress]] = Field(alias="host", default=None,discriminator="odata_type", )
	sslCertificate: Optional[SecuritySslCertificate] = Field(alias="sslCertificate", default=None,)

from .security_host_ssl_certificate_port import SecurityHostSslCertificatePort
from .security_hostname import SecurityHostname
from .security_ip_address import SecurityIpAddress
from .security_ssl_certificate import SecuritySslCertificate
