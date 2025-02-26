from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityHostSslCertificatePort(BaseModel):
	firstSeenDateTime: Optional[datetime] = Field(default=None,alias="firstSeenDateTime",)
	lastSeenDateTime: Optional[datetime] = Field(default=None,alias="lastSeenDateTime",)
	port: Optional[int] = Field(default=None,alias="port",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


