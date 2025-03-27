from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class OsVersionCount(BaseModel):
	deviceCount: Optional[int] = Field(alias="deviceCount", default=None,)
	lastUpdateDateTime: Optional[datetime] = Field(alias="lastUpdateDateTime", default=None,)
	osVersion: Optional[str] = Field(alias="osVersion", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


