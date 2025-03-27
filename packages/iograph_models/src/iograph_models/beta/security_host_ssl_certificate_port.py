from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityHostSslCertificatePort(BaseModel):
	firstSeenDateTime: Optional[datetime] = Field(alias="firstSeenDateTime", default=None,)
	lastSeenDateTime: Optional[datetime] = Field(alias="lastSeenDateTime", default=None,)
	port: Optional[int] = Field(alias="port", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


