from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class DeviceGeoLocation(BaseModel):
	altitude: Optional[float] | Optional[str] | ReferenceNumeric
	heading: Optional[float] | Optional[str] | ReferenceNumeric
	horizontalAccuracy: Optional[float] | Optional[str] | ReferenceNumeric
	lastCollectedDateTime: Optional[datetime] = Field(default=None,alias="lastCollectedDateTime",)
	latitude: Optional[float] | Optional[str] | ReferenceNumeric
	longitude: Optional[float] | Optional[str] | ReferenceNumeric
	speed: Optional[float] | Optional[str] | ReferenceNumeric
	verticalAccuracy: Optional[float] | Optional[str] | ReferenceNumeric
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric

