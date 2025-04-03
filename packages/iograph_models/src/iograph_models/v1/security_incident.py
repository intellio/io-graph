from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityIncident(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.security.incident"] = Field(alias="@odata.type", default="#microsoft.graph.security.incident")
	assignedTo: Optional[str] = Field(alias="assignedTo", default=None,)
	classification: Optional[SecurityAlertClassification | str] = Field(alias="classification", default=None,)
	comments: Optional[list[SecurityAlertComment]] = Field(alias="comments", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	customTags: Optional[list[str]] = Field(alias="customTags", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	determination: Optional[SecurityAlertDetermination | str] = Field(alias="determination", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	incidentWebUrl: Optional[str] = Field(alias="incidentWebUrl", default=None,)
	lastModifiedBy: Optional[str] = Field(alias="lastModifiedBy", default=None,)
	lastUpdateDateTime: Optional[datetime] = Field(alias="lastUpdateDateTime", default=None,)
	redirectIncidentId: Optional[str] = Field(alias="redirectIncidentId", default=None,)
	resolvingComment: Optional[str] = Field(alias="resolvingComment", default=None,)
	severity: Optional[SecurityAlertSeverity | str] = Field(alias="severity", default=None,)
	status: Optional[SecurityIncidentStatus | str] = Field(alias="status", default=None,)
	summary: Optional[str] = Field(alias="summary", default=None,)
	systemTags: Optional[list[str]] = Field(alias="systemTags", default=None,)
	tenantId: Optional[str] = Field(alias="tenantId", default=None,)
	alerts: Optional[list[SecurityAlert]] = Field(alias="alerts", default=None,)

from .security_alert_classification import SecurityAlertClassification
from .security_alert_comment import SecurityAlertComment
from .security_alert_determination import SecurityAlertDetermination
from .security_alert_severity import SecurityAlertSeverity
from .security_incident_status import SecurityIncidentStatus
from .security_alert import SecurityAlert
