from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WebPartPosition(BaseModel):
	columnId: float | str | ReferenceNumeric
	horizontalSectionId: float | str | ReferenceNumeric
	isInVerticalSection: Optional[bool] = Field(default=None,alias="isInVerticalSection",)
	webPartIndex: float | str | ReferenceNumeric
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric

