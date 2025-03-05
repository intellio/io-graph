from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class UserTrainingContentEventInfo(BaseModel):
	browser: Optional[str] = Field(default=None,alias="browser",)
	contentDateTime: Optional[datetime] = Field(default=None,alias="contentDateTime",)
	ipAddress: Optional[str] = Field(default=None,alias="ipAddress",)
	osPlatformDeviceDetails: Optional[str] = Field(default=None,alias="osPlatformDeviceDetails",)
	potentialScoreImpact: float | str | ReferenceNumeric
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .reference_numeric import ReferenceNumeric

