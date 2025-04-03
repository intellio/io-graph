from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class HardwareConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.hardwareConfiguration"] = Field(alias="@odata.type", default="#microsoft.graph.hardwareConfiguration")
	configurationFileContent: Optional[str] = Field(alias="configurationFileContent", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	fileName: Optional[str] = Field(alias="fileName", default=None,)
	hardwareConfigurationFormat: Optional[HardwareConfigurationFormat | str] = Field(alias="hardwareConfigurationFormat", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	perDevicePasswordDisabled: Optional[bool] = Field(alias="perDevicePasswordDisabled", default=None,)
	roleScopeTagIds: Optional[list[str]] = Field(alias="roleScopeTagIds", default=None,)
	version: Optional[int] = Field(alias="version", default=None,)
	assignments: Optional[list[HardwareConfigurationAssignment]] = Field(alias="assignments", default=None,)
	deviceRunStates: Optional[list[HardwareConfigurationDeviceState]] = Field(alias="deviceRunStates", default=None,)
	runSummary: Optional[HardwareConfigurationRunSummary] = Field(alias="runSummary", default=None,)
	userRunStates: Optional[list[HardwareConfigurationUserState]] = Field(alias="userRunStates", default=None,)

from .hardware_configuration_format import HardwareConfigurationFormat
from .hardware_configuration_assignment import HardwareConfigurationAssignment
from .hardware_configuration_device_state import HardwareConfigurationDeviceState
from .hardware_configuration_run_summary import HardwareConfigurationRunSummary
from .hardware_configuration_user_state import HardwareConfigurationUserState
