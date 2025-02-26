from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityThreatIntelligence(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	articleIndicators: list[SecurityArticleIndicator] = Field(alias="articleIndicators",)
	articles: list[SecurityArticle] = Field(alias="articles",)
	hostComponents: list[SecurityHostComponent] = Field(alias="hostComponents",)
	hostCookies: list[SecurityHostCookie] = Field(alias="hostCookies",)
	hostPairs: list[SecurityHostPair] = Field(alias="hostPairs",)
	hostPorts: list[SecurityHostPort] = Field(alias="hostPorts",)
	hosts: list[SecurityHost] = Field(alias="hosts",)
	hostSslCertificates: list[SecurityHostSslCertificate] = Field(alias="hostSslCertificates",)
	hostTrackers: list[SecurityHostTracker] = Field(alias="hostTrackers",)
	intelligenceProfileIndicators: list[SecurityIntelligenceProfileIndicator] = Field(alias="intelligenceProfileIndicators",)
	intelProfiles: list[SecurityIntelligenceProfile] = Field(alias="intelProfiles",)
	passiveDnsRecords: list[SecurityPassiveDnsRecord] = Field(alias="passiveDnsRecords",)
	sslCertificates: list[SecuritySslCertificate] = Field(alias="sslCertificates",)
	subdomains: list[SecuritySubdomain] = Field(alias="subdomains",)
	vulnerabilities: list[SecurityVulnerability] = Field(alias="vulnerabilities",)
	whoisHistoryRecords: list[SecurityWhoisHistoryRecord] = Field(alias="whoisHistoryRecords",)
	whoisRecords: list[SecurityWhoisRecord] = Field(alias="whoisRecords",)

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

