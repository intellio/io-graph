from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityHostPort(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.security.hostPort"] = Field(alias="@odata.type",)
	banners: Optional[list[SecurityHostPortBanner]] = Field(alias="banners", default=None,)
	firstSeenDateTime: Optional[datetime] = Field(alias="firstSeenDateTime", default=None,)
	lastScanDateTime: Optional[datetime] = Field(alias="lastScanDateTime", default=None,)
	lastSeenDateTime: Optional[datetime] = Field(alias="lastSeenDateTime", default=None,)
	port: Optional[int] = Field(alias="port", default=None,)
	protocol: Optional[SecurityHostPortProtocol | str] = Field(alias="protocol", default=None,)
	services: Optional[list[SecurityHostPortComponent]] = Field(alias="services", default=None,)
	status: Optional[SecurityHostPortStatus | str] = Field(alias="status", default=None,)
	timesObserved: Optional[int] = Field(alias="timesObserved", default=None,)
	host: Optional[Union[SecurityHostname, SecurityIpAddress]] = Field(alias="host", default=None,discriminator="odata_type", )
	mostRecentSslCertificate: Optional[SecuritySslCertificate] = Field(alias="mostRecentSslCertificate", default=None,)

from .security_host_port_banner import SecurityHostPortBanner
from .security_host_port_protocol import SecurityHostPortProtocol
from .security_host_port_component import SecurityHostPortComponent
from .security_host_port_status import SecurityHostPortStatus
from .security_hostname import SecurityHostname
from .security_ip_address import SecurityIpAddress
from .security_ssl_certificate import SecuritySslCertificate
