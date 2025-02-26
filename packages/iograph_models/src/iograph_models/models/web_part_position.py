from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WebPartPosition(BaseModel):
	columnId: Optional[float] | Optional[str] | ReferenceNumeric
	horizontalSectionId: Optional[float] | Optional[str] | ReferenceNumeric
	isInVerticalSection: Optional[bool] = Field(default=None,alias="isInVerticalSection",)
	webPartIndex: Optional[float] | Optional[str] | ReferenceNumeric
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric

