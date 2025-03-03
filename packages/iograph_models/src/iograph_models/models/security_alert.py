from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityAlert(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	actorDisplayName: Optional[str] = Field(default=None,alias="actorDisplayName",)
	additionalData: Optional[SecurityDictionary] = Field(default=None,alias="additionalData",)
	alertPolicyId: Optional[str] = Field(default=None,alias="alertPolicyId",)
	alertWebUrl: Optional[str] = Field(default=None,alias="alertWebUrl",)
	assignedTo: Optional[str] = Field(default=None,alias="assignedTo",)
	category: Optional[str] = Field(default=None,alias="category",)
	classification: Optional[SecurityAlertClassification] = Field(default=None,alias="classification",)
	comments: Optional[list[SecurityAlertComment]] = Field(default=None,alias="comments",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	detectionSource: Optional[SecurityDetectionSource] = Field(default=None,alias="detectionSource",)
	detectorId: Optional[str] = Field(default=None,alias="detectorId",)
	determination: Optional[SecurityAlertDetermination] = Field(default=None,alias="determination",)
	evidence: Optional[list[SecurityAlertEvidence]] = Field(default=None,alias="evidence",)
	firstActivityDateTime: Optional[datetime] = Field(default=None,alias="firstActivityDateTime",)
	incidentId: Optional[str] = Field(default=None,alias="incidentId",)
	incidentWebUrl: Optional[str] = Field(default=None,alias="incidentWebUrl",)
	lastActivityDateTime: Optional[datetime] = Field(default=None,alias="lastActivityDateTime",)
	lastUpdateDateTime: Optional[datetime] = Field(default=None,alias="lastUpdateDateTime",)
	mitreTechniques: Optional[list[str]] = Field(default=None,alias="mitreTechniques",)
	productName: Optional[str] = Field(default=None,alias="productName",)
	providerAlertId: Optional[str] = Field(default=None,alias="providerAlertId",)
	recommendedActions: Optional[str] = Field(default=None,alias="recommendedActions",)
	resolvedDateTime: Optional[datetime] = Field(default=None,alias="resolvedDateTime",)
	serviceSource: Optional[SecurityServiceSource] = Field(default=None,alias="serviceSource",)
	severity: Optional[SecurityAlertSeverity] = Field(default=None,alias="severity",)
	status: Optional[SecurityAlertStatus] = Field(default=None,alias="status",)
	systemTags: Optional[list[str]] = Field(default=None,alias="systemTags",)
	tenantId: Optional[str] = Field(default=None,alias="tenantId",)
	threatDisplayName: Optional[str] = Field(default=None,alias="threatDisplayName",)
	threatFamilyName: Optional[str] = Field(default=None,alias="threatFamilyName",)
	title: Optional[str] = Field(default=None,alias="title",)

from .security_dictionary import SecurityDictionary
from .security_alert_classification import SecurityAlertClassification
from .security_alert_comment import SecurityAlertComment
from .security_detection_source import SecurityDetectionSource
from .security_alert_determination import SecurityAlertDetermination
from .security_alert_evidence import SecurityAlertEvidence
from .security_service_source import SecurityServiceSource
from .security_alert_severity import SecurityAlertSeverity
from .security_alert_status import SecurityAlertStatus

