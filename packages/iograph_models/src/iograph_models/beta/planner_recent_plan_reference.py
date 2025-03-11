from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class PlannerRecentPlanReference(BaseModel):
	lastAccessedDateTime: Optional[datetime] = Field(alias="lastAccessedDateTime",default=None,)
	planTitle: Optional[str] = Field(alias="planTitle",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


