from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class DeviceHealthScriptDeviceState(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.deviceHealthScriptDeviceState"] = Field(alias="@odata.type",)
	assignmentFilterIds: Optional[list[str]] = Field(alias="assignmentFilterIds", default=None,)
	detectionState: Optional[RunState | str] = Field(alias="detectionState", default=None,)
	expectedStateUpdateDateTime: Optional[datetime] = Field(alias="expectedStateUpdateDateTime", default=None,)
	lastStateUpdateDateTime: Optional[datetime] = Field(alias="lastStateUpdateDateTime", default=None,)
	lastSyncDateTime: Optional[datetime] = Field(alias="lastSyncDateTime", default=None,)
	postRemediationDetectionScriptError: Optional[str] = Field(alias="postRemediationDetectionScriptError", default=None,)
	postRemediationDetectionScriptOutput: Optional[str] = Field(alias="postRemediationDetectionScriptOutput", default=None,)
	preRemediationDetectionScriptError: Optional[str] = Field(alias="preRemediationDetectionScriptError", default=None,)
	preRemediationDetectionScriptOutput: Optional[str] = Field(alias="preRemediationDetectionScriptOutput", default=None,)
	remediationScriptError: Optional[str] = Field(alias="remediationScriptError", default=None,)
	remediationState: Optional[RemediationState | str] = Field(alias="remediationState", default=None,)
	managedDevice: Optional[Union[WindowsManagedDevice]] = Field(alias="managedDevice", default=None,discriminator="odata_type", )

from .run_state import RunState
from .remediation_state import RemediationState
from .windows_managed_device import WindowsManagedDevice
