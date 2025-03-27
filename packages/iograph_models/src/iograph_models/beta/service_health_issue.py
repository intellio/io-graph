from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ServiceHealthIssue(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.serviceHealthIssue"] = Field(alias="@odata.type", default="#microsoft.graph.serviceHealthIssue")
	details: Optional[list[KeyValuePair]] = Field(alias="details", default=None,)
	endDateTime: Optional[datetime] = Field(alias="endDateTime", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime", default=None,)
	title: Optional[str] = Field(alias="title", default=None,)
	classification: Optional[ServiceHealthClassificationType | str] = Field(alias="classification", default=None,)
	feature: Optional[str] = Field(alias="feature", default=None,)
	featureGroup: Optional[str] = Field(alias="featureGroup", default=None,)
	impactDescription: Optional[str] = Field(alias="impactDescription", default=None,)
	isResolved: Optional[bool] = Field(alias="isResolved", default=None,)
	origin: Optional[ServiceHealthOrigin | str] = Field(alias="origin", default=None,)
	posts: Optional[list[ServiceHealthIssuePost]] = Field(alias="posts", default=None,)
	service: Optional[str] = Field(alias="service", default=None,)
	status: Optional[ServiceHealthStatus | str] = Field(alias="status", default=None,)

from .key_value_pair import KeyValuePair
from .service_health_classification_type import ServiceHealthClassificationType
from .service_health_origin import ServiceHealthOrigin
from .service_health_issue_post import ServiceHealthIssuePost
from .service_health_status import ServiceHealthStatus

