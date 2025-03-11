from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UserExperienceAnalyticsImpactingProcess(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	category: Optional[str] = Field(alias="category",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	deviceId: Optional[str] = Field(alias="deviceId",default=None,)
	impactValue: float | str | ReferenceNumeric
	processName: Optional[str] = Field(alias="processName",default=None,)
	publisher: Optional[str] = Field(alias="publisher",default=None,)

from .reference_numeric import ReferenceNumeric

