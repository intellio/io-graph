from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WebPartPosition(BaseModel):
	columnId: float | str | ReferenceNumeric
	horizontalSectionId: float | str | ReferenceNumeric
	isInVerticalSection: Optional[bool] = Field(alias="isInVerticalSection", default=None,)
	webPartIndex: float | str | ReferenceNumeric
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .reference_numeric import ReferenceNumeric
