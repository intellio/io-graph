from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityHostPair(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	firstSeenDateTime: Optional[datetime] = Field(alias="firstSeenDateTime",default=None,)
	lastSeenDateTime: Optional[datetime] = Field(alias="lastSeenDateTime",default=None,)
	linkKind: Optional[str] = Field(alias="linkKind",default=None,)
	childHost: SerializeAsAny[Optional[SecurityHost]] = Field(alias="childHost",default=None,)
	parentHost: SerializeAsAny[Optional[SecurityHost]] = Field(alias="parentHost",default=None,)

from .security_host import SecurityHost
from .security_host import SecurityHost

