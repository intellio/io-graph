from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TeamworkOnPremisesCalendarSyncConfiguration(BaseModel):
	domain: Optional[str] = Field(alias="domain",default=None,)
	domainUserName: Optional[str] = Field(alias="domainUserName",default=None,)
	smtpAddress: Optional[str] = Field(alias="smtpAddress",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


