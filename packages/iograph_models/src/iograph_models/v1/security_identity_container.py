from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityIdentityContainer(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	healthIssues: Optional[list[SecurityHealthIssue]] = Field(alias="healthIssues",default=None,)
	sensors: Optional[list[SecuritySensor]] = Field(alias="sensors",default=None,)

from .security_health_issue import SecurityHealthIssue
from .security_sensor import SecuritySensor

