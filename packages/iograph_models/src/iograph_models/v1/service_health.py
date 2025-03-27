from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ServiceHealth(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	service: Optional[str] = Field(alias="service", default=None,)
	status: Optional[ServiceHealthStatus | str] = Field(alias="status", default=None,)
	issues: Optional[list[ServiceHealthIssue]] = Field(alias="issues", default=None,)

from .service_health_status import ServiceHealthStatus
from .service_health_issue import ServiceHealthIssue

