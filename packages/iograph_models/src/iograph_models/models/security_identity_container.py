from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityIdentityContainer(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	healthIssues: Optional[list[SecurityHealthIssue]] = Field(default=None,alias="healthIssues",)
	sensors: Optional[list[SecuritySensor]] = Field(default=None,alias="sensors",)

from .security_health_issue import SecurityHealthIssue
from .security_sensor import SecuritySensor

