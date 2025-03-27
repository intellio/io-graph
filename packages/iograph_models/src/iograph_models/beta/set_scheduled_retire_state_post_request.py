from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Set_scheduled_retire_statePostRequest(BaseModel):
	scopedToAllDevices: Optional[bool] = Field(alias="scopedToAllDevices", default=None,)
	state: Optional[ScheduledRetireState | str] = Field(alias="state", default=None,)
	managedDeviceIds: Optional[list[str]] = Field(alias="managedDeviceIds", default=None,)

from .scheduled_retire_state import ScheduledRetireState

