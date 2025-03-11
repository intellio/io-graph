from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsAutopilotDeploymentProfileCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: SerializeAsAny[Optional[list[WindowsAutopilotDeploymentProfile]]] = Field(alias="value",default=None,)

from .windows_autopilot_deployment_profile import WindowsAutopilotDeploymentProfile

