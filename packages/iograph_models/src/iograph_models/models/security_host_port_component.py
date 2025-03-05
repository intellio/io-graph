from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityHostPortComponent(BaseModel):
	firstSeenDateTime: Optional[datetime] = Field(default=None,alias="firstSeenDateTime",)
	isRecent: Optional[bool] = Field(default=None,alias="isRecent",)
	lastSeenDateTime: Optional[datetime] = Field(default=None,alias="lastSeenDateTime",)
	component: Optional[SecurityHostComponent] = Field(default=None,alias="component",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .security_host_component import SecurityHostComponent

