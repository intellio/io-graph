from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityPassiveDnsRecord(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	collectedDateTime: Optional[datetime] = Field(default=None,alias="collectedDateTime",)
	firstSeenDateTime: Optional[datetime] = Field(default=None,alias="firstSeenDateTime",)
	lastSeenDateTime: Optional[datetime] = Field(default=None,alias="lastSeenDateTime",)
	recordType: Optional[str] = Field(default=None,alias="recordType",)
	artifact: Optional[SecurityArtifact] = Field(default=None,alias="artifact",)
	parentHost: Optional[SecurityHost] = Field(default=None,alias="parentHost",)

from .security_artifact import SecurityArtifact
from .security_host import SecurityHost

