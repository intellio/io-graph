from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class DeviceManagementScript(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.deviceManagementScript"] = Field(alias="@odata.type", default="#microsoft.graph.deviceManagementScript")
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	enforceSignatureCheck: Optional[bool] = Field(alias="enforceSignatureCheck", default=None,)
	fileName: Optional[str] = Field(alias="fileName", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	roleScopeTagIds: Optional[list[str]] = Field(alias="roleScopeTagIds", default=None,)
	runAs32Bit: Optional[bool] = Field(alias="runAs32Bit", default=None,)
	runAsAccount: Optional[RunAsAccountType | str] = Field(alias="runAsAccount", default=None,)
	scriptContent: Optional[str] = Field(alias="scriptContent", default=None,)
	assignments: Optional[list[DeviceManagementScriptAssignment]] = Field(alias="assignments", default=None,)
	deviceRunStates: Optional[list[DeviceManagementScriptDeviceState]] = Field(alias="deviceRunStates", default=None,)
	groupAssignments: Optional[list[DeviceManagementScriptGroupAssignment]] = Field(alias="groupAssignments", default=None,)
	runSummary: Optional[DeviceManagementScriptRunSummary] = Field(alias="runSummary", default=None,)
	userRunStates: Optional[list[DeviceManagementScriptUserState]] = Field(alias="userRunStates", default=None,)

from .run_as_account_type import RunAsAccountType
from .device_management_script_assignment import DeviceManagementScriptAssignment
from .device_management_script_device_state import DeviceManagementScriptDeviceState
from .device_management_script_group_assignment import DeviceManagementScriptGroupAssignment
from .device_management_script_run_summary import DeviceManagementScriptRunSummary
from .device_management_script_user_state import DeviceManagementScriptUserState
