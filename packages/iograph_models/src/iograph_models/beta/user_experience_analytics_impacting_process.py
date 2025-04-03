from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class UserExperienceAnalyticsImpactingProcess(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.userExperienceAnalyticsImpactingProcess"] = Field(alias="@odata.type", default="#microsoft.graph.userExperienceAnalyticsImpactingProcess")
	category: Optional[str] = Field(alias="category", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	deviceId: Optional[str] = Field(alias="deviceId", default=None,)
	impactValue: float | str | ReferenceNumeric
	processName: Optional[str] = Field(alias="processName", default=None,)
	publisher: Optional[str] = Field(alias="publisher", default=None,)

from .reference_numeric import ReferenceNumeric
