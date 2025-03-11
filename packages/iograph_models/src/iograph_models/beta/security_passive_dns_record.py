from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityPassiveDnsRecord(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	collectedDateTime: Optional[datetime] = Field(alias="collectedDateTime",default=None,)
	firstSeenDateTime: Optional[datetime] = Field(alias="firstSeenDateTime",default=None,)
	lastSeenDateTime: Optional[datetime] = Field(alias="lastSeenDateTime",default=None,)
	recordType: Optional[str] = Field(alias="recordType",default=None,)
	artifact: SerializeAsAny[Optional[SecurityArtifact]] = Field(alias="artifact",default=None,)
	parentHost: SerializeAsAny[Optional[SecurityHost]] = Field(alias="parentHost",default=None,)

from .security_artifact import SecurityArtifact
from .security_host import SecurityHost

