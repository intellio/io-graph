from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ServiceHealth(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	service: Optional[str] = Field(default=None,alias="service",)
	status: Optional[ServiceHealthStatus] = Field(default=None,alias="status",)
	issues: Optional[list[ServiceHealthIssue]] = Field(default=None,alias="issues",)

from .service_health_status import ServiceHealthStatus
from .service_health_issue import ServiceHealthIssue

