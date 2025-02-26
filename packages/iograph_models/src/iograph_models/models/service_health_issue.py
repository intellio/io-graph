from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class ServiceHealthIssue(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	details: list[KeyValuePair] = Field(alias="details",)
	endDateTime: Optional[datetime] = Field(default=None,alias="endDateTime",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	startDateTime: Optional[datetime] = Field(default=None,alias="startDateTime",)
	title: Optional[str] = Field(default=None,alias="title",)
	classification: Optional[ServiceHealthClassificationType] = Field(default=None,alias="classification",)
	feature: Optional[str] = Field(default=None,alias="feature",)
	featureGroup: Optional[str] = Field(default=None,alias="featureGroup",)
	impactDescription: Optional[str] = Field(default=None,alias="impactDescription",)
	isResolved: Optional[bool] = Field(default=None,alias="isResolved",)
	origin: Optional[ServiceHealthOrigin] = Field(default=None,alias="origin",)
	posts: list[ServiceHealthIssuePost] = Field(alias="posts",)
	service: Optional[str] = Field(default=None,alias="service",)
	status: Optional[ServiceHealthStatus] = Field(default=None,alias="status",)

from .key_value_pair import KeyValuePair
from .service_health_classification_type import ServiceHealthClassificationType
from .service_health_origin import ServiceHealthOrigin
from .service_health_issue_post import ServiceHealthIssuePost
from .service_health_status import ServiceHealthStatus

