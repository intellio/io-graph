from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityWhoisHistoryRecord(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.security.whoisHistoryRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.whoisHistoryRecord")
	abuse: Optional[SecurityWhoisContact] = Field(alias="abuse", default=None,)
	admin: Optional[SecurityWhoisContact] = Field(alias="admin", default=None,)
	billing: Optional[SecurityWhoisContact] = Field(alias="billing", default=None,)
	domainStatus: Optional[str] = Field(alias="domainStatus", default=None,)
	expirationDateTime: Optional[datetime] = Field(alias="expirationDateTime", default=None,)
	firstSeenDateTime: Optional[datetime] = Field(alias="firstSeenDateTime", default=None,)
	lastSeenDateTime: Optional[datetime] = Field(alias="lastSeenDateTime", default=None,)
	lastUpdateDateTime: Optional[datetime] = Field(alias="lastUpdateDateTime", default=None,)
	nameservers: Optional[list[SecurityWhoisNameserver]] = Field(alias="nameservers", default=None,)
	noc: Optional[SecurityWhoisContact] = Field(alias="noc", default=None,)
	rawWhoisText: Optional[str] = Field(alias="rawWhoisText", default=None,)
	registrant: Optional[SecurityWhoisContact] = Field(alias="registrant", default=None,)
	registrar: Optional[SecurityWhoisContact] = Field(alias="registrar", default=None,)
	registrationDateTime: Optional[datetime] = Field(alias="registrationDateTime", default=None,)
	technical: Optional[SecurityWhoisContact] = Field(alias="technical", default=None,)
	whoisServer: Optional[str] = Field(alias="whoisServer", default=None,)
	zone: Optional[SecurityWhoisContact] = Field(alias="zone", default=None,)
	host: Optional[Union[SecurityHostname, SecurityIpAddress]] = Field(alias="host", default=None,discriminator="odata_type", )

from .security_whois_contact import SecurityWhoisContact
from .security_whois_nameserver import SecurityWhoisNameserver
from .security_hostname import SecurityHostname
from .security_ip_address import SecurityIpAddress
