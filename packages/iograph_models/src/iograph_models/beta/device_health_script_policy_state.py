from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceHealthScriptPolicyState(BaseModel):
	assignmentFilterIds: Optional[list[str]] = Field(alias="assignmentFilterIds", default=None,)
	detectionState: Optional[RunState | str] = Field(alias="detectionState", default=None,)
	deviceId: Optional[str] = Field(alias="deviceId", default=None,)
	deviceName: Optional[str] = Field(alias="deviceName", default=None,)
	expectedStateUpdateDateTime: Optional[datetime] = Field(alias="expectedStateUpdateDateTime", default=None,)
	id: Optional[str] = Field(alias="id", default=None,)
	lastStateUpdateDateTime: Optional[datetime] = Field(alias="lastStateUpdateDateTime", default=None,)
	lastSyncDateTime: Optional[datetime] = Field(alias="lastSyncDateTime", default=None,)
	osVersion: Optional[str] = Field(alias="osVersion", default=None,)
	policyId: Optional[str] = Field(alias="policyId", default=None,)
	policyName: Optional[str] = Field(alias="policyName", default=None,)
	postRemediationDetectionScriptError: Optional[str] = Field(alias="postRemediationDetectionScriptError", default=None,)
	postRemediationDetectionScriptOutput: Optional[str] = Field(alias="postRemediationDetectionScriptOutput", default=None,)
	preRemediationDetectionScriptError: Optional[str] = Field(alias="preRemediationDetectionScriptError", default=None,)
	preRemediationDetectionScriptOutput: Optional[str] = Field(alias="preRemediationDetectionScriptOutput", default=None,)
	remediationScriptError: Optional[str] = Field(alias="remediationScriptError", default=None,)
	remediationState: Optional[RemediationState | str] = Field(alias="remediationState", default=None,)
	userName: Optional[str] = Field(alias="userName", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .run_state import RunState
from .remediation_state import RemediationState

