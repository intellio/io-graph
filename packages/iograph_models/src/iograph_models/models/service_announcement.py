from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ServiceAnnouncement(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	healthOverviews: list[ServiceHealth] = Field(alias="healthOverviews",)
	issues: list[ServiceHealthIssue] = Field(alias="issues",)
	messages: list[ServiceUpdateMessage] = Field(alias="messages",)

from .service_health import ServiceHealth
from .service_health_issue import ServiceHealthIssue
from .service_update_message import ServiceUpdateMessage

