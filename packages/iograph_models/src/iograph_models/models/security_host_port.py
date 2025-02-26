from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityHostPort(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	banners: list[SecurityHostPortBanner] = Field(alias="banners",)
	firstSeenDateTime: Optional[datetime] = Field(default=None,alias="firstSeenDateTime",)
	lastScanDateTime: Optional[datetime] = Field(default=None,alias="lastScanDateTime",)
	lastSeenDateTime: Optional[datetime] = Field(default=None,alias="lastSeenDateTime",)
	port: Optional[int] = Field(default=None,alias="port",)
	protocol: Optional[SecurityHostPortProtocol] = Field(default=None,alias="protocol",)
	services: list[SecurityHostPortComponent] = Field(alias="services",)
	status: Optional[SecurityHostPortStatus] = Field(default=None,alias="status",)
	timesObserved: Optional[int] = Field(default=None,alias="timesObserved",)
	host: Optional[SecurityHost] = Field(default=None,alias="host",)
	mostRecentSslCertificate: Optional[SecuritySslCertificate] = Field(default=None,alias="mostRecentSslCertificate",)

from .security_host_port_banner import SecurityHostPortBanner
from .security_host_port_protocol import SecurityHostPortProtocol
from .security_host_port_component import SecurityHostPortComponent
from .security_host_port_status import SecurityHostPortStatus
from .security_host import SecurityHost
from .security_ssl_certificate import SecuritySslCertificate

