from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityHostname(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	firstSeenDateTime: Optional[datetime] = Field(default=None,alias="firstSeenDateTime",)
	lastSeenDateTime: Optional[datetime] = Field(default=None,alias="lastSeenDateTime",)
	childHostPairs: list[SecurityHostPair] = Field(alias="childHostPairs",)
	components: list[SecurityHostComponent] = Field(alias="components",)
	cookies: list[SecurityHostCookie] = Field(alias="cookies",)
	hostPairs: list[SecurityHostPair] = Field(alias="hostPairs",)
	parentHostPairs: list[SecurityHostPair] = Field(alias="parentHostPairs",)
	passiveDns: list[SecurityPassiveDnsRecord] = Field(alias="passiveDns",)
	passiveDnsReverse: list[SecurityPassiveDnsRecord] = Field(alias="passiveDnsReverse",)
	ports: list[SecurityHostPort] = Field(alias="ports",)
	reputation: Optional[SecurityHostReputation] = Field(default=None,alias="reputation",)
	sslCertificates: list[SecurityHostSslCertificate] = Field(alias="sslCertificates",)
	subdomains: list[SecuritySubdomain] = Field(alias="subdomains",)
	trackers: list[SecurityHostTracker] = Field(alias="trackers",)
	whois: Optional[SecurityWhoisRecord] = Field(default=None,alias="whois",)
	registrant: Optional[str] = Field(default=None,alias="registrant",)
	registrar: Optional[str] = Field(default=None,alias="registrar",)

from .security_host_pair import SecurityHostPair
from .security_host_component import SecurityHostComponent
from .security_host_cookie import SecurityHostCookie
from .security_host_pair import SecurityHostPair
from .security_host_pair import SecurityHostPair
from .security_passive_dns_record import SecurityPassiveDnsRecord
from .security_passive_dns_record import SecurityPassiveDnsRecord
from .security_host_port import SecurityHostPort
from .security_host_reputation import SecurityHostReputation
from .security_host_ssl_certificate import SecurityHostSslCertificate
from .security_subdomain import SecuritySubdomain
from .security_host_tracker import SecurityHostTracker
from .security_whois_record import SecurityWhoisRecord

