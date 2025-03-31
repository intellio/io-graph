from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityIntelligenceProfileIndicator(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.security.intelligenceProfileIndicator"] = Field(alias="@odata.type", default="#microsoft.graph.security.intelligenceProfileIndicator")
	source: Optional[SecurityIndicatorSource | str] = Field(alias="source", default=None,)
	artifact: Optional[Union[SecurityHostname, SecurityIpAddress, SecurityHostComponent, SecurityHostCookie, SecurityHostSslCertificate, SecurityHostTracker, SecurityPassiveDnsRecord, SecuritySslCertificate, SecurityUnclassifiedArtifact]] = Field(alias="artifact", default=None,discriminator="odata_type", )
	firstSeenDateTime: Optional[datetime] = Field(alias="firstSeenDateTime", default=None,)
	lastSeenDateTime: Optional[datetime] = Field(alias="lastSeenDateTime", default=None,)

from .security_indicator_source import SecurityIndicatorSource
from .security_hostname import SecurityHostname
from .security_ip_address import SecurityIpAddress
from .security_host_component import SecurityHostComponent
from .security_host_cookie import SecurityHostCookie
from .security_host_ssl_certificate import SecurityHostSslCertificate
from .security_host_tracker import SecurityHostTracker
from .security_passive_dns_record import SecurityPassiveDnsRecord
from .security_ssl_certificate import SecuritySslCertificate
from .security_unclassified_artifact import SecurityUnclassifiedArtifact
