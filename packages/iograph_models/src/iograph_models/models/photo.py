from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class Photo(BaseModel):
	cameraMake: Optional[str] = Field(default=None,alias="cameraMake",)
	cameraModel: Optional[str] = Field(default=None,alias="cameraModel",)
	exposureDenominator: Optional[float] | Optional[str] | ReferenceNumeric
	exposureNumerator: Optional[float] | Optional[str] | ReferenceNumeric
	fNumber: Optional[float] | Optional[str] | ReferenceNumeric
	focalLength: Optional[float] | Optional[str] | ReferenceNumeric
	iso: Optional[int] = Field(default=None,alias="iso",)
	orientation: Optional[int] = Field(default=None,alias="orientation",)
	takenDateTime: Optional[datetime] = Field(default=None,alias="takenDateTime",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric

