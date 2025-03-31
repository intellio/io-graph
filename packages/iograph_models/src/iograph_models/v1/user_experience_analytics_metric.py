from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class UserExperienceAnalyticsMetric(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.userExperienceAnalyticsMetric"] = Field(alias="@odata.type",)
	unit: Optional[str] = Field(alias="unit", default=None,)
	value: float | str | ReferenceNumeric

from .reference_numeric import ReferenceNumeric
