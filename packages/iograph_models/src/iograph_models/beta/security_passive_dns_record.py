from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityPassiveDnsRecord(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.security.passiveDnsRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.passiveDnsRecord")
	collectedDateTime: Optional[datetime] = Field(alias="collectedDateTime", default=None,)
	firstSeenDateTime: Optional[datetime] = Field(alias="firstSeenDateTime", default=None,)
	lastSeenDateTime: Optional[datetime] = Field(alias="lastSeenDateTime", default=None,)
	recordType: Optional[str] = Field(alias="recordType", default=None,)
	artifact: Optional[Union[SecurityHost, SecurityHostname, SecurityIpAddress, SecurityHostComponent, SecurityHostCookie, SecurityHostSslCertificate, SecurityHostTracker, SecurityPassiveDnsRecord, SecuritySslCertificate, SecurityUnclassifiedArtifact]] = Field(alias="artifact", default=None,discriminator="odata_type", )
	parentHost: Optional[Union[SecurityHostname, SecurityIpAddress]] = Field(alias="parentHost", default=None,discriminator="odata_type", )

from .security_host import SecurityHost
from .security_hostname import SecurityHostname
from .security_ip_address import SecurityIpAddress
from .security_host_component import SecurityHostComponent
from .security_host_cookie import SecurityHostCookie
from .security_host_ssl_certificate import SecurityHostSslCertificate
from .security_host_tracker import SecurityHostTracker
from .security_ssl_certificate import SecuritySslCertificate
from .security_unclassified_artifact import SecurityUnclassifiedArtifact
from .security_hostname import SecurityHostname
from .security_ip_address import SecurityIpAddress

