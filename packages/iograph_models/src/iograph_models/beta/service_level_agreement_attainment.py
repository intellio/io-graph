from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ServiceLevelAgreementAttainment(BaseModel):
	endDate: Optional[str] = Field(alias="endDate", default=None,)
	score: float | str | ReferenceNumeric
	startDate: Optional[str] = Field(alias="startDate", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .reference_numeric import ReferenceNumeric
