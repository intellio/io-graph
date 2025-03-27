from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceHealthScript(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	detectionScriptContent: Optional[str] = Field(alias="detectionScriptContent", default=None,)
	detectionScriptParameters: Optional[list[Annotated[Union[DeviceHealthScriptBooleanParameter, DeviceHealthScriptIntegerParameter, DeviceHealthScriptStringParameter]],Field(discriminator="odata_type")]]] = Field(alias="detectionScriptParameters", default=None,)
	deviceHealthScriptType: Optional[DeviceHealthScriptType | str] = Field(alias="deviceHealthScriptType", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	enforceSignatureCheck: Optional[bool] = Field(alias="enforceSignatureCheck", default=None,)
	highestAvailableVersion: Optional[str] = Field(alias="highestAvailableVersion", default=None,)
	isGlobalScript: Optional[bool] = Field(alias="isGlobalScript", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	publisher: Optional[str] = Field(alias="publisher", default=None,)
	remediationScriptContent: Optional[str] = Field(alias="remediationScriptContent", default=None,)
	remediationScriptParameters: Optional[list[Annotated[Union[DeviceHealthScriptBooleanParameter, DeviceHealthScriptIntegerParameter, DeviceHealthScriptStringParameter]],Field(discriminator="odata_type")]]] = Field(alias="remediationScriptParameters", default=None,)
	roleScopeTagIds: Optional[list[str]] = Field(alias="roleScopeTagIds", default=None,)
	runAs32Bit: Optional[bool] = Field(alias="runAs32Bit", default=None,)
	runAsAccount: Optional[RunAsAccountType | str] = Field(alias="runAsAccount", default=None,)
	version: Optional[str] = Field(alias="version", default=None,)
	assignments: Optional[list[DeviceHealthScriptAssignment]] = Field(alias="assignments", default=None,)
	deviceRunStates: Optional[list[DeviceHealthScriptDeviceState]] = Field(alias="deviceRunStates", default=None,)
	runSummary: Optional[DeviceHealthScriptRunSummary] = Field(alias="runSummary", default=None,)

from .device_health_script_boolean_parameter import DeviceHealthScriptBooleanParameter
from .device_health_script_integer_parameter import DeviceHealthScriptIntegerParameter
from .device_health_script_string_parameter import DeviceHealthScriptStringParameter
from .device_health_script_type import DeviceHealthScriptType
from .device_health_script_boolean_parameter import DeviceHealthScriptBooleanParameter
from .device_health_script_integer_parameter import DeviceHealthScriptIntegerParameter
from .device_health_script_string_parameter import DeviceHealthScriptStringParameter
from .run_as_account_type import RunAsAccountType
from .device_health_script_assignment import DeviceHealthScriptAssignment
from .device_health_script_device_state import DeviceHealthScriptDeviceState
from .device_health_script_run_summary import DeviceHealthScriptRunSummary

