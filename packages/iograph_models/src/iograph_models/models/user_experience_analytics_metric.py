from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UserExperienceAnalyticsMetric(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	unit: Optional[str] = Field(default=None,alias="unit",)
	value: float | str | ReferenceNumeric

from .reference_numeric import ReferenceNumeric

