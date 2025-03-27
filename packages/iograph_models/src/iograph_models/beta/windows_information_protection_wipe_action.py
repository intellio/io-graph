from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsInformationProtectionWipeAction(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	lastCheckInDateTime: Optional[datetime] = Field(alias="lastCheckInDateTime", default=None,)
	status: Optional[ActionState | str] = Field(alias="status", default=None,)
	targetedDeviceMacAddress: Optional[str] = Field(alias="targetedDeviceMacAddress", default=None,)
	targetedDeviceName: Optional[str] = Field(alias="targetedDeviceName", default=None,)
	targetedDeviceRegistrationId: Optional[str] = Field(alias="targetedDeviceRegistrationId", default=None,)
	targetedUserId: Optional[str] = Field(alias="targetedUserId", default=None,)

from .action_state import ActionState

