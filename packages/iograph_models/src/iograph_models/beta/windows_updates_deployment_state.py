from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WindowsUpdatesDeploymentState(BaseModel):
	effectiveValue: Optional[WindowsUpdatesDeploymentStateValue | str] = Field(alias="effectiveValue", default=None,)
	reasons: Optional[list[WindowsUpdatesDeploymentStateReason]] = Field(alias="reasons", default=None,)
	requestedValue: Optional[WindowsUpdatesRequestedDeploymentStateValue | str] = Field(alias="requestedValue", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .windows_updates_deployment_state_value import WindowsUpdatesDeploymentStateValue
from .windows_updates_deployment_state_reason import WindowsUpdatesDeploymentStateReason
from .windows_updates_requested_deployment_state_value import WindowsUpdatesRequestedDeploymentStateValue
