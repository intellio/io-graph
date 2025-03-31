from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityHostname(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.security.hostname"] = Field(alias="@odata.type", default="#microsoft.graph.security.hostname")
	firstSeenDateTime: Optional[datetime] = Field(alias="firstSeenDateTime", default=None,)
	lastSeenDateTime: Optional[datetime] = Field(alias="lastSeenDateTime", default=None,)
	childHostPairs: Optional[list[SecurityHostPair]] = Field(alias="childHostPairs", default=None,)
	components: Optional[list[SecurityHostComponent]] = Field(alias="components", default=None,)
	cookies: Optional[list[SecurityHostCookie]] = Field(alias="cookies", default=None,)
	hostPairs: Optional[list[SecurityHostPair]] = Field(alias="hostPairs", default=None,)
	parentHostPairs: Optional[list[SecurityHostPair]] = Field(alias="parentHostPairs", default=None,)
	passiveDns: Optional[list[SecurityPassiveDnsRecord]] = Field(alias="passiveDns", default=None,)
	passiveDnsReverse: Optional[list[SecurityPassiveDnsRecord]] = Field(alias="passiveDnsReverse", default=None,)
	ports: Optional[list[SecurityHostPort]] = Field(alias="ports", default=None,)
	reputation: Optional[SecurityHostReputation] = Field(alias="reputation", default=None,)
	sslCertificates: Optional[list[SecurityHostSslCertificate]] = Field(alias="sslCertificates", default=None,)
	subdomains: Optional[list[SecuritySubdomain]] = Field(alias="subdomains", default=None,)
	trackers: Optional[list[SecurityHostTracker]] = Field(alias="trackers", default=None,)
	whois: Optional[SecurityWhoisRecord] = Field(alias="whois", default=None,)
	registrant: Optional[str] = Field(alias="registrant", default=None,)
	registrar: Optional[str] = Field(alias="registrar", default=None,)

from .security_host_pair import SecurityHostPair
from .security_host_component import SecurityHostComponent
from .security_host_cookie import SecurityHostCookie
from .security_passive_dns_record import SecurityPassiveDnsRecord
from .security_host_port import SecurityHostPort
from .security_host_reputation import SecurityHostReputation
from .security_host_ssl_certificate import SecurityHostSslCertificate
from .security_subdomain import SecuritySubdomain
from .security_host_tracker import SecurityHostTracker
from .security_whois_record import SecurityWhoisRecord
