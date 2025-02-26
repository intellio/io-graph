from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SynchronizationProgress(BaseModel):
	completedUnits: Optional[int] = Field(default=None,alias="completedUnits",)
	progressObservationDateTime: Optional[datetime] = Field(default=None,alias="progressObservationDateTime",)
	totalUnits: Optional[int] = Field(default=None,alias="totalUnits",)
	units: Optional[str] = Field(default=None,alias="units",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


