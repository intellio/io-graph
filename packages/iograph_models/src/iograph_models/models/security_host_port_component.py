from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityHostPortComponent(BaseModel):
	firstSeenDateTime: Optional[datetime] = Field(alias="firstSeenDateTime",default=None,)
	isRecent: Optional[bool] = Field(alias="isRecent",default=None,)
	lastSeenDateTime: Optional[datetime] = Field(alias="lastSeenDateTime",default=None,)
	component: Optional[SecurityHostComponent] = Field(alias="component",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .security_host_component import SecurityHostComponent

