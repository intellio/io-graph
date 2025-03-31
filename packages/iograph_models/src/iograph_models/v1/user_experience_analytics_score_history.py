from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class UserExperienceAnalyticsScoreHistory(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.userExperienceAnalyticsScoreHistory"] = Field(alias="@odata.type",)
	startupDateTime: Optional[datetime] = Field(alias="startupDateTime", default=None,)

