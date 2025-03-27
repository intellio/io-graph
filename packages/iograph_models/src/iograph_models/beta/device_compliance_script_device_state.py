from __future__ import annotations
from typing import Optional
from typing import Union
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceComplianceScriptDeviceState(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	detectionState: Optional[RunState | str] = Field(alias="detectionState", default=None,)
	expectedStateUpdateDateTime: Optional[datetime] = Field(alias="expectedStateUpdateDateTime", default=None,)
	lastStateUpdateDateTime: Optional[datetime] = Field(alias="lastStateUpdateDateTime", default=None,)
	lastSyncDateTime: Optional[datetime] = Field(alias="lastSyncDateTime", default=None,)
	scriptError: Optional[str] = Field(alias="scriptError", default=None,)
	scriptOutput: Optional[str] = Field(alias="scriptOutput", default=None,)
	managedDevice: Optional[Union[WindowsManagedDevice]] = Field(alias="managedDevice", default=None,discriminator="odata_type", )

from .run_state import RunState
from .windows_managed_device import WindowsManagedDevice

