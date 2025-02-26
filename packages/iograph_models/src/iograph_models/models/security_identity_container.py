from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityIdentityContainer(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	healthIssues: list[SecurityHealthIssue] = Field(alias="healthIssues",)
	sensors: list[SecuritySensor] = Field(alias="sensors",)

from .security_health_issue import SecurityHealthIssue
from .security_sensor import SecuritySensor

