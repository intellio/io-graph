from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class WindowsDefenderApplicationControlSupplementalPolicyDeploymentSummary(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.windowsDefenderApplicationControlSupplementalPolicyDeploymentSummary"] = Field(alias="@odata.type", default="#microsoft.graph.windowsDefenderApplicationControlSupplementalPolicyDeploymentSummary")
	deployedDeviceCount: Optional[int] = Field(alias="deployedDeviceCount", default=None,)
	failedDeviceCount: Optional[int] = Field(alias="failedDeviceCount", default=None,)

