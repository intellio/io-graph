from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IdentityGovernanceLifecycleManagementSettings(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	emailSettings: Optional[EmailSettings] = Field(default=None,alias="emailSettings",)
	workflowScheduleIntervalInHours: Optional[int] = Field(default=None,alias="workflowScheduleIntervalInHours",)

from .email_settings import EmailSettings

