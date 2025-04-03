from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class WindowsInformationProtectionWipeAction(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.windowsInformationProtectionWipeAction"] = Field(alias="@odata.type", default="#microsoft.graph.windowsInformationProtectionWipeAction")
	lastCheckInDateTime: Optional[datetime] = Field(alias="lastCheckInDateTime", default=None,)
	status: Optional[ActionState | str] = Field(alias="status", default=None,)
	targetedDeviceMacAddress: Optional[str] = Field(alias="targetedDeviceMacAddress", default=None,)
	targetedDeviceName: Optional[str] = Field(alias="targetedDeviceName", default=None,)
	targetedDeviceRegistrationId: Optional[str] = Field(alias="targetedDeviceRegistrationId", default=None,)
	targetedUserId: Optional[str] = Field(alias="targetedUserId", default=None,)

from .action_state import ActionState
