from __future__ import annotations
from uuid import UUID
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityAttackSimulationInfo(BaseModel):
	attackSimDateTime: Optional[datetime] = Field(alias="attackSimDateTime", default=None,)
	attackSimDurationTime: Optional[str] = Field(alias="attackSimDurationTime", default=None,)
	attackSimId: Optional[UUID] = Field(alias="attackSimId", default=None,)
	attackSimUserId: Optional[str] = Field(alias="attackSimUserId", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

