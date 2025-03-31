from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ServiceAnnouncement(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.serviceAnnouncement"] = Field(alias="@odata.type",)
	healthOverviews: Optional[list[ServiceHealth]] = Field(alias="healthOverviews", default=None,)
	issues: Optional[list[ServiceHealthIssue]] = Field(alias="issues", default=None,)
	messages: Optional[list[ServiceUpdateMessage]] = Field(alias="messages", default=None,)

from .service_health import ServiceHealth
from .service_health_issue import ServiceHealthIssue
from .service_update_message import ServiceUpdateMessage
