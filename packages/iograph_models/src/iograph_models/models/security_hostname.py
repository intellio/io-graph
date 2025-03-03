from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityHostname(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	firstSeenDateTime: Optional[datetime] = Field(default=None,alias="firstSeenDateTime",)
	lastSeenDateTime: Optional[datetime] = Field(default=None,alias="lastSeenDateTime",)
	childHostPairs: Optional[list[SecurityHostPair]] = Field(default=None,alias="childHostPairs",)
	components: Optional[list[SecurityHostComponent]] = Field(default=None,alias="components",)
	cookies: Optional[list[SecurityHostCookie]] = Field(default=None,alias="cookies",)
	hostPairs: Optional[list[SecurityHostPair]] = Field(default=None,alias="hostPairs",)
	parentHostPairs: Optional[list[SecurityHostPair]] = Field(default=None,alias="parentHostPairs",)
	passiveDns: Optional[list[SecurityPassiveDnsRecord]] = Field(default=None,alias="passiveDns",)
	passiveDnsReverse: Optional[list[SecurityPassiveDnsRecord]] = Field(default=None,alias="passiveDnsReverse",)
	ports: Optional[list[SecurityHostPort]] = Field(default=None,alias="ports",)
	reputation: Optional[SecurityHostReputation] = Field(default=None,alias="reputation",)
	sslCertificates: Optional[list[SecurityHostSslCertificate]] = Field(default=None,alias="sslCertificates",)
	subdomains: Optional[list[SecuritySubdomain]] = Field(default=None,alias="subdomains",)
	trackers: Optional[list[SecurityHostTracker]] = Field(default=None,alias="trackers",)
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

