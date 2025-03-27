from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Photo(BaseModel):
	cameraMake: Optional[str] = Field(alias="cameraMake", default=None,)
	cameraModel: Optional[str] = Field(alias="cameraModel", default=None,)
	exposureDenominator: float | str | ReferenceNumeric
	exposureNumerator: float | str | ReferenceNumeric
	fNumber: float | str | ReferenceNumeric
	focalLength: float | str | ReferenceNumeric
	iso: Optional[int] = Field(alias="iso", default=None,)
	orientation: Optional[int] = Field(alias="orientation", default=None,)
	takenDateTime: Optional[datetime] = Field(alias="takenDateTime", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric

