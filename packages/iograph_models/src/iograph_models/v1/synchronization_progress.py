from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SynchronizationProgress(BaseModel):
	completedUnits: Optional[int] = Field(alias="completedUnits",default=None,)
	progressObservationDateTime: Optional[datetime] = Field(alias="progressObservationDateTime",default=None,)
	totalUnits: Optional[int] = Field(alias="totalUnits",default=None,)
	units: Optional[str] = Field(alias="units",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


