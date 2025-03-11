from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceComplianceScript(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	detectionScriptContent: Optional[str] = Field(alias="detectionScriptContent",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	enforceSignatureCheck: Optional[bool] = Field(alias="enforceSignatureCheck",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	publisher: Optional[str] = Field(alias="publisher",default=None,)
	roleScopeTagIds: Optional[list[str]] = Field(alias="roleScopeTagIds",default=None,)
	runAs32Bit: Optional[bool] = Field(alias="runAs32Bit",default=None,)
	runAsAccount: Optional[RunAsAccountType | str] = Field(alias="runAsAccount",default=None,)
	version: Optional[str] = Field(alias="version",default=None,)
	assignments: Optional[list[DeviceHealthScriptAssignment]] = Field(alias="assignments",default=None,)
	deviceRunStates: Optional[list[DeviceComplianceScriptDeviceState]] = Field(alias="deviceRunStates",default=None,)
	runSummary: Optional[DeviceComplianceScriptRunSummary] = Field(alias="runSummary",default=None,)

from .run_as_account_type import RunAsAccountType
from .device_health_script_assignment import DeviceHealthScriptAssignment
from .device_compliance_script_device_state import DeviceComplianceScriptDeviceState
from .device_compliance_script_run_summary import DeviceComplianceScriptRunSummary

