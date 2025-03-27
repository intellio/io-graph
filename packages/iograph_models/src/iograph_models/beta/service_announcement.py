from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ServiceAnnouncement(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	healthOverviews: Optional[list[ServiceHealth]] = Field(alias="healthOverviews", default=None,)
	issues: Optional[list[ServiceHealthIssue]] = Field(alias="issues", default=None,)
	messages: Optional[list[ServiceUpdateMessage]] = Field(alias="messages", default=None,)

from .service_health import ServiceHealth
from .service_health_issue import ServiceHealthIssue
from .service_update_message import ServiceUpdateMessage

