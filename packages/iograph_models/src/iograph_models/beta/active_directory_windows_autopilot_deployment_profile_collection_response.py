from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ActiveDirectoryWindowsAutopilotDeploymentProfileCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[ActiveDirectoryWindowsAutopilotDeploymentProfile]] = Field(alias="value",default=None,)

from .active_directory_windows_autopilot_deployment_profile import ActiveDirectoryWindowsAutopilotDeploymentProfile

