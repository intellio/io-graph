from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IdentityGovernanceLifecycleManagementSettings(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	emailSettings: Optional[EmailSettings] = Field(alias="emailSettings", default=None,)
	workflowScheduleIntervalInHours: Optional[int] = Field(alias="workflowScheduleIntervalInHours", default=None,)

from .email_settings import EmailSettings

