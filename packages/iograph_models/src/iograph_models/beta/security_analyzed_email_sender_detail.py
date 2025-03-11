from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityAnalyzedEmailSenderDetail(BaseModel):
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	domainCreationDateTime: Optional[datetime] = Field(alias="domainCreationDateTime",default=None,)
	domainName: Optional[str] = Field(alias="domainName",default=None,)
	domainOwner: Optional[str] = Field(alias="domainOwner",default=None,)
	fromAddress: Optional[str] = Field(alias="fromAddress",default=None,)
	ipv4: Optional[str] = Field(alias="ipv4",default=None,)
	location: Optional[str] = Field(alias="location",default=None,)
	mailFromAddress: Optional[str] = Field(alias="mailFromAddress",default=None,)
	mailFromDomainName: Optional[str] = Field(alias="mailFromDomainName",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


