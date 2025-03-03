from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityWhoisHistoryRecord(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	abuse: Optional[SecurityWhoisContact] = Field(default=None,alias="abuse",)
	admin: Optional[SecurityWhoisContact] = Field(default=None,alias="admin",)
	billing: Optional[SecurityWhoisContact] = Field(default=None,alias="billing",)
	domainStatus: Optional[str] = Field(default=None,alias="domainStatus",)
	expirationDateTime: Optional[datetime] = Field(default=None,alias="expirationDateTime",)
	firstSeenDateTime: Optional[datetime] = Field(default=None,alias="firstSeenDateTime",)
	lastSeenDateTime: Optional[datetime] = Field(default=None,alias="lastSeenDateTime",)
	lastUpdateDateTime: Optional[datetime] = Field(default=None,alias="lastUpdateDateTime",)
	nameservers: Optional[list[SecurityWhoisNameserver]] = Field(default=None,alias="nameservers",)
	noc: Optional[SecurityWhoisContact] = Field(default=None,alias="noc",)
	rawWhoisText: Optional[str] = Field(default=None,alias="rawWhoisText",)
	registrant: Optional[SecurityWhoisContact] = Field(default=None,alias="registrant",)
	registrar: Optional[SecurityWhoisContact] = Field(default=None,alias="registrar",)
	registrationDateTime: Optional[datetime] = Field(default=None,alias="registrationDateTime",)
	technical: Optional[SecurityWhoisContact] = Field(default=None,alias="technical",)
	whoisServer: Optional[str] = Field(default=None,alias="whoisServer",)
	zone: Optional[SecurityWhoisContact] = Field(default=None,alias="zone",)
	host: Optional[SecurityHost] = Field(default=None,alias="host",)

from .security_whois_contact import SecurityWhoisContact
from .security_whois_contact import SecurityWhoisContact
from .security_whois_contact import SecurityWhoisContact
from .security_whois_nameserver import SecurityWhoisNameserver
from .security_whois_contact import SecurityWhoisContact
from .security_whois_contact import SecurityWhoisContact
from .security_whois_contact import SecurityWhoisContact
from .security_whois_contact import SecurityWhoisContact
from .security_whois_contact import SecurityWhoisContact
from .security_host import SecurityHost

