from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class PlannerPlanContext(BaseModel):
	associationType: Optional[str] = Field(alias="associationType", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	displayNameSegments: Optional[list[str]] = Field(alias="displayNameSegments", default=None,)
	isCreationContext: Optional[bool] = Field(alias="isCreationContext", default=None,)
	ownerAppId: Optional[str] = Field(alias="ownerAppId", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

