from __future__ import annotations
from typing import Optional
from typing import Union
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementScriptDeviceState(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	errorCode: Optional[int] = Field(alias="errorCode", default=None,)
	errorDescription: Optional[str] = Field(alias="errorDescription", default=None,)
	lastStateUpdateDateTime: Optional[datetime] = Field(alias="lastStateUpdateDateTime", default=None,)
	resultMessage: Optional[str] = Field(alias="resultMessage", default=None,)
	runState: Optional[RunState | str] = Field(alias="runState", default=None,)
	managedDevice: Optional[Union[WindowsManagedDevice]] = Field(alias="managedDevice", default=None,discriminator="odata_type", )

from .run_state import RunState
from .windows_managed_device import WindowsManagedDevice

