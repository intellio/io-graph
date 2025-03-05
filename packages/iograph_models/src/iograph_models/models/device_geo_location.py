from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceGeoLocation(BaseModel):
	altitude: float | str | ReferenceNumeric
	heading: float | str | ReferenceNumeric
	horizontalAccuracy: float | str | ReferenceNumeric
	lastCollectedDateTime: Optional[datetime] = Field(default=None,alias="lastCollectedDateTime",)
	latitude: float | str | ReferenceNumeric
	longitude: float | str | ReferenceNumeric
	speed: float | str | ReferenceNumeric
	verticalAccuracy: float | str | ReferenceNumeric
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric

