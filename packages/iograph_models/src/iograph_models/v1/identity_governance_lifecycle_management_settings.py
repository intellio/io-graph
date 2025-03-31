from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class IdentityGovernanceLifecycleManagementSettings(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.identityGovernance.lifecycleManagementSettings"] = Field(alias="@odata.type",)
	emailSettings: Optional[EmailSettings] = Field(alias="emailSettings", default=None,)
	workflowScheduleIntervalInHours: Optional[int] = Field(alias="workflowScheduleIntervalInHours", default=None,)

from .email_settings import EmailSettings
