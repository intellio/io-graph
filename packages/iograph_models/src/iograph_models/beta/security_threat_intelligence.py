from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from pydantic import BaseModel, Field


class SecurityThreatIntelligence(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.security.threatIntelligence"] = Field(alias="@odata.type", default="#microsoft.graph.security.threatIntelligence")
	articleIndicators: Optional[list[SecurityArticleIndicator]] = Field(alias="articleIndicators", default=None,)
	articles: Optional[list[SecurityArticle]] = Field(alias="articles", default=None,)
	hostComponents: Optional[list[SecurityHostComponent]] = Field(alias="hostComponents", default=None,)
	hostCookies: Optional[list[SecurityHostCookie]] = Field(alias="hostCookies", default=None,)
	hostPairs: Optional[list[SecurityHostPair]] = Field(alias="hostPairs", default=None,)
	hostPorts: Optional[list[SecurityHostPort]] = Field(alias="hostPorts", default=None,)
	hosts: Optional[list[Annotated[Union[SecurityHostname, SecurityIpAddress],Field(discriminator="odata_type")]]] = Field(alias="hosts", default=None,)
	hostSslCertificates: Optional[list[SecurityHostSslCertificate]] = Field(alias="hostSslCertificates", default=None,)
	hostTrackers: Optional[list[SecurityHostTracker]] = Field(alias="hostTrackers", default=None,)
	intelligenceProfileIndicators: Optional[list[SecurityIntelligenceProfileIndicator]] = Field(alias="intelligenceProfileIndicators", default=None,)
	intelProfiles: Optional[list[SecurityIntelligenceProfile]] = Field(alias="intelProfiles", default=None,)
	passiveDnsRecords: Optional[list[SecurityPassiveDnsRecord]] = Field(alias="passiveDnsRecords", default=None,)
	sslCertificates: Optional[list[SecuritySslCertificate]] = Field(alias="sslCertificates", default=None,)
	subdomains: Optional[list[SecuritySubdomain]] = Field(alias="subdomains", default=None,)
	vulnerabilities: Optional[list[SecurityVulnerability]] = Field(alias="vulnerabilities", default=None,)
	whoisHistoryRecords: Optional[list[SecurityWhoisHistoryRecord]] = Field(alias="whoisHistoryRecords", default=None,)
	whoisRecords: Optional[list[SecurityWhoisRecord]] = Field(alias="whoisRecords", default=None,)

from .security_article_indicator import SecurityArticleIndicator
from .security_article import SecurityArticle
from .security_host_component import SecurityHostComponent
from .security_host_cookie import SecurityHostCookie
from .security_host_pair import SecurityHostPair
from .security_host_port import SecurityHostPort
from .security_hostname import SecurityHostname
from .security_ip_address import SecurityIpAddress
from .security_host_ssl_certificate import SecurityHostSslCertificate
from .security_host_tracker import SecurityHostTracker
from .security_intelligence_profile_indicator import SecurityIntelligenceProfileIndicator
from .security_intelligence_profile import SecurityIntelligenceProfile
from .security_passive_dns_record import SecurityPassiveDnsRecord
from .security_ssl_certificate import SecuritySslCertificate
from .security_subdomain import SecuritySubdomain
from .security_vulnerability import SecurityVulnerability
from .security_whois_history_record import SecurityWhoisHistoryRecord
from .security_whois_record import SecurityWhoisRecord
