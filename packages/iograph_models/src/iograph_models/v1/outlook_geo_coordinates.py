from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OutlookGeoCoordinates(BaseModel):
	accuracy: float | str | ReferenceNumeric
	altitude: float | str | ReferenceNumeric
	altitudeAccuracy: float | str | ReferenceNumeric
	latitude: float | str | ReferenceNumeric
	longitude: float | str | ReferenceNumeric
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric

