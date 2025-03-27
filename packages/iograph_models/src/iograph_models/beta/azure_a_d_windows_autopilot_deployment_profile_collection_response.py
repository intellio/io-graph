from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AzureADWindowsAutopilotDeploymentProfileCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[AzureADWindowsAutopilotDeploymentProfile]] = Field(alias="value", default=None,)

from .azure_a_d_windows_autopilot_deployment_profile import AzureADWindowsAutopilotDeploymentProfile

