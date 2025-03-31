from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class DeviceGeoLocation(BaseModel):
	altitude: float | str | ReferenceNumeric
	heading: float | str | ReferenceNumeric
	horizontalAccuracy: float | str | ReferenceNumeric
	lastCollectedDateTime: Optional[datetime] = Field(alias="lastCollectedDateTime", default=None,)
	latitude: float | str | ReferenceNumeric
	longitude: float | str | ReferenceNumeric
	speed: float | str | ReferenceNumeric
	verticalAccuracy: float | str | ReferenceNumeric
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .reference_numeric import ReferenceNumeric
