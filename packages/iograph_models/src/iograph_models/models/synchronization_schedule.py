from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SynchronizationSchedule(BaseModel):
	expiration: Optional[datetime] = Field(alias="expiration",default=None,)
	interval: Optional[str] = Field(alias="interval",default=None,)
	state: Optional[str | SynchronizationScheduleState] = Field(alias="state",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .synchronization_schedule_state import SynchronizationScheduleState

