from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceHealthScriptDeviceState(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	assignmentFilterIds: Optional[list[str]] = Field(alias="assignmentFilterIds",default=None,)
	detectionState: Optional[RunState | str] = Field(alias="detectionState",default=None,)
	expectedStateUpdateDateTime: Optional[datetime] = Field(alias="expectedStateUpdateDateTime",default=None,)
	lastStateUpdateDateTime: Optional[datetime] = Field(alias="lastStateUpdateDateTime",default=None,)
	lastSyncDateTime: Optional[datetime] = Field(alias="lastSyncDateTime",default=None,)
	postRemediationDetectionScriptError: Optional[str] = Field(alias="postRemediationDetectionScriptError",default=None,)
	postRemediationDetectionScriptOutput: Optional[str] = Field(alias="postRemediationDetectionScriptOutput",default=None,)
	preRemediationDetectionScriptError: Optional[str] = Field(alias="preRemediationDetectionScriptError",default=None,)
	preRemediationDetectionScriptOutput: Optional[str] = Field(alias="preRemediationDetectionScriptOutput",default=None,)
	remediationScriptError: Optional[str] = Field(alias="remediationScriptError",default=None,)
	remediationState: Optional[RemediationState | str] = Field(alias="remediationState",default=None,)
	managedDevice: SerializeAsAny[Optional[ManagedDevice]] = Field(alias="managedDevice",default=None,)

from .run_state import RunState
from .remediation_state import RemediationState
from .managed_device import ManagedDevice

