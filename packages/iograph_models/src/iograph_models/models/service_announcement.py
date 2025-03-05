from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ServiceAnnouncement(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	healthOverviews: Optional[list[ServiceHealth]] = Field(default=None,alias="healthOverviews",)
	issues: Optional[list[ServiceHealthIssue]] = Field(default=None,alias="issues",)
	messages: Optional[list[ServiceUpdateMessage]] = Field(default=None,alias="messages",)

from .service_health import ServiceHealth
from .service_health_issue import ServiceHealthIssue
from .service_update_message import ServiceUpdateMessage

