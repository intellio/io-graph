from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityIncident(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	assignedTo: Optional[str] = Field(default=None,alias="assignedTo",)
	classification: Optional[SecurityAlertClassification] = Field(default=None,alias="classification",)
	comments: list[SecurityAlertComment] = Field(alias="comments",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	customTags: list[Optional[str]] = Field(alias="customTags",)
	description: Optional[str] = Field(default=None,alias="description",)
	determination: Optional[SecurityAlertDetermination] = Field(default=None,alias="determination",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	incidentWebUrl: Optional[str] = Field(default=None,alias="incidentWebUrl",)
	lastModifiedBy: Optional[str] = Field(default=None,alias="lastModifiedBy",)
	lastUpdateDateTime: Optional[datetime] = Field(default=None,alias="lastUpdateDateTime",)
	redirectIncidentId: Optional[str] = Field(default=None,alias="redirectIncidentId",)
	resolvingComment: Optional[str] = Field(default=None,alias="resolvingComment",)
	severity: Optional[SecurityAlertSeverity] = Field(default=None,alias="severity",)
	status: Optional[SecurityIncidentStatus] = Field(default=None,alias="status",)
	summary: Optional[str] = Field(default=None,alias="summary",)
	systemTags: list[Optional[str]] = Field(alias="systemTags",)
	tenantId: Optional[str] = Field(default=None,alias="tenantId",)
	alerts: list[SecurityAlert] = Field(alias="alerts",)

from .security_alert_classification import SecurityAlertClassification
from .security_alert_comment import SecurityAlertComment
from .security_alert_determination import SecurityAlertDetermination
from .security_alert_severity import SecurityAlertSeverity
from .security_incident_status import SecurityIncidentStatus
from .security_alert import SecurityAlert

