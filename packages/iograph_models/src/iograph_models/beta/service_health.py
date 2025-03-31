from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ServiceHealth(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.serviceHealth"] = Field(alias="@odata.type",)
	service: Optional[str] = Field(alias="service", default=None,)
	status: Optional[ServiceHealthStatus | str] = Field(alias="status", default=None,)
	issues: Optional[list[ServiceHealthIssue]] = Field(alias="issues", default=None,)

from .service_health_status import ServiceHealthStatus
from .service_health_issue import ServiceHealthIssue
