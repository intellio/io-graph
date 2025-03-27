from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class UserTrainingContentEventInfo(BaseModel):
	browser: Optional[str] = Field(alias="browser", default=None,)
	contentDateTime: Optional[datetime] = Field(alias="contentDateTime", default=None,)
	ipAddress: Optional[str] = Field(alias="ipAddress", default=None,)
	osPlatformDeviceDetails: Optional[str] = Field(alias="osPlatformDeviceDetails", default=None,)
	potentialScoreImpact: float | str | ReferenceNumeric
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .reference_numeric import ReferenceNumeric

