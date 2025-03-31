from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class HardwareConfigurationDeviceState(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.hardwareConfigurationDeviceState"] = Field(alias="@odata.type",)
	assignmentFilterIds: Optional[str] = Field(alias="assignmentFilterIds", default=None,)
	configurationError: Optional[str] = Field(alias="configurationError", default=None,)
	configurationOutput: Optional[str] = Field(alias="configurationOutput", default=None,)
	configurationState: Optional[RunState | str] = Field(alias="configurationState", default=None,)
	deviceName: Optional[str] = Field(alias="deviceName", default=None,)
	internalVersion: Optional[int] = Field(alias="internalVersion", default=None,)
	lastStateUpdateDateTime: Optional[datetime] = Field(alias="lastStateUpdateDateTime", default=None,)
	osVersion: Optional[str] = Field(alias="osVersion", default=None,)
	upn: Optional[str] = Field(alias="upn", default=None,)
	userId: Optional[str] = Field(alias="userId", default=None,)

from .run_state import RunState
