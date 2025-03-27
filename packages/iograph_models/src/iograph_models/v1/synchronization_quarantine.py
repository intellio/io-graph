from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SynchronizationQuarantine(BaseModel):
	currentBegan: Optional[datetime] = Field(alias="currentBegan", default=None,)
	error: Optional[SynchronizationError] = Field(alias="error", default=None,)
	nextAttempt: Optional[datetime] = Field(alias="nextAttempt", default=None,)
	reason: Optional[QuarantineReason | str] = Field(alias="reason", default=None,)
	seriesBegan: Optional[datetime] = Field(alias="seriesBegan", default=None,)
	seriesCount: Optional[int] = Field(alias="seriesCount", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .synchronization_error import SynchronizationError
from .quarantine_reason import QuarantineReason

