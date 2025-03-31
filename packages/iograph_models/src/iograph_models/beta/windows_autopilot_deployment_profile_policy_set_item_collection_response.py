from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WindowsAutopilotDeploymentProfilePolicySetItemCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[WindowsAutopilotDeploymentProfilePolicySetItem]] = Field(alias="value", default=None,)

from .windows_autopilot_deployment_profile_policy_set_item import WindowsAutopilotDeploymentProfilePolicySetItem
