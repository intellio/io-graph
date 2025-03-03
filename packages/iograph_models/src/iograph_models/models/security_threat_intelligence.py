from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityThreatIntelligence(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	articleIndicators: Optional[list[SecurityArticleIndicator]] = Field(default=None,alias="articleIndicators",)
	articles: Optional[list[SecurityArticle]] = Field(default=None,alias="articles",)
	hostComponents: Optional[list[SecurityHostComponent]] = Field(default=None,alias="hostComponents",)
	hostCookies: Optional[list[SecurityHostCookie]] = Field(default=None,alias="hostCookies",)
	hostPairs: Optional[list[SecurityHostPair]] = Field(default=None,alias="hostPairs",)
	hostPorts: Optional[list[SecurityHostPort]] = Field(default=None,alias="hostPorts",)
	hosts: Optional[list[SecurityHost]] = Field(default=None,alias="hosts",)
	hostSslCertificates: Optional[list[SecurityHostSslCertificate]] = Field(default=None,alias="hostSslCertificates",)
	hostTrackers: Optional[list[SecurityHostTracker]] = Field(default=None,alias="hostTrackers",)
	intelligenceProfileIndicators: Optional[list[SecurityIntelligenceProfileIndicator]] = Field(default=None,alias="intelligenceProfileIndicators",)
	intelProfiles: Optional[list[SecurityIntelligenceProfile]] = Field(default=None,alias="intelProfiles",)
	passiveDnsRecords: Optional[list[SecurityPassiveDnsRecord]] = Field(default=None,alias="passiveDnsRecords",)
	sslCertificates: Optional[list[SecuritySslCertificate]] = Field(default=None,alias="sslCertificates",)
	subdomains: Optional[list[SecuritySubdomain]] = Field(default=None,alias="subdomains",)
	vulnerabilities: Optional[list[SecurityVulnerability]] = Field(default=None,alias="vulnerabilities",)
	whoisHistoryRecords: Optional[list[SecurityWhoisHistoryRecord]] = Field(default=None,alias="whoisHistoryRecords",)
	whoisRecords: Optional[list[SecurityWhoisRecord]] = Field(default=None,alias="whoisRecords",)

from .security_article_indicator import SecurityArticleIndicator
from .security_article import SecurityArticle
from .security_host_component import SecurityHostComponent
from .security_host_cookie import SecurityHostCookie
from .security_host_pair import SecurityHostPair
from .security_host_port import SecurityHostPort
from .security_host import SecurityHost
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

