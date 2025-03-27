from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UserExperienceAnalyticsMetric(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	unit: Optional[str] = Field(alias="unit", default=None,)
	value: float | str | ReferenceNumeric

from .reference_numeric import ReferenceNumeric

