from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SynchronizationSchedule(BaseModel):
	expiration: Optional[datetime] = Field(default=None,alias="expiration",)
	interval: Optional[str] = Field(default=None,alias="interval",)
	state: Optional[SynchronizationScheduleState] = Field(default=None,alias="state",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .synchronization_schedule_state import SynchronizationScheduleState

