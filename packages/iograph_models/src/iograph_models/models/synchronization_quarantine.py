from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SynchronizationQuarantine(BaseModel):
	currentBegan: Optional[datetime] = Field(default=None,alias="currentBegan",)
	error: Optional[SynchronizationError] = Field(default=None,alias="error",)
	nextAttempt: Optional[datetime] = Field(default=None,alias="nextAttempt",)
	reason: Optional[QuarantineReason] = Field(default=None,alias="reason",)
	seriesBegan: Optional[datetime] = Field(default=None,alias="seriesBegan",)
	seriesCount: Optional[int] = Field(default=None,alias="seriesCount",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .synchronization_error import SynchronizationError
from .quarantine_reason import QuarantineReason

