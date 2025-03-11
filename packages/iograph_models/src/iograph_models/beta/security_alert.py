from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityAlert(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	actorDisplayName: Optional[str] = Field(alias="actorDisplayName",default=None,)
	additionalData: Optional[SecurityDictionary] = Field(alias="additionalData",default=None,)
	alertPolicyId: Optional[str] = Field(alias="alertPolicyId",default=None,)
	alertWebUrl: Optional[str] = Field(alias="alertWebUrl",default=None,)
	assignedTo: Optional[str] = Field(alias="assignedTo",default=None,)
	category: Optional[str] = Field(alias="category",default=None,)
	classification: Optional[SecurityAlertClassification | str] = Field(alias="classification",default=None,)
	comments: Optional[list[SecurityAlertComment]] = Field(alias="comments",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	detectionSource: Optional[SecurityDetectionSource | str] = Field(alias="detectionSource",default=None,)
	detectorId: Optional[str] = Field(alias="detectorId",default=None,)
	determination: Optional[SecurityAlertDetermination | str] = Field(alias="determination",default=None,)
	evidence: SerializeAsAny[Optional[list[SecurityAlertEvidence]]] = Field(alias="evidence",default=None,)
	firstActivityDateTime: Optional[datetime] = Field(alias="firstActivityDateTime",default=None,)
	incidentId: Optional[str] = Field(alias="incidentId",default=None,)
	incidentWebUrl: Optional[str] = Field(alias="incidentWebUrl",default=None,)
	lastActivityDateTime: Optional[datetime] = Field(alias="lastActivityDateTime",default=None,)
	lastUpdateDateTime: Optional[datetime] = Field(alias="lastUpdateDateTime",default=None,)
	mitreTechniques: Optional[list[str]] = Field(alias="mitreTechniques",default=None,)
	productName: Optional[str] = Field(alias="productName",default=None,)
	providerAlertId: Optional[str] = Field(alias="providerAlertId",default=None,)
	recommendedActions: Optional[str] = Field(alias="recommendedActions",default=None,)
	resolvedDateTime: Optional[datetime] = Field(alias="resolvedDateTime",default=None,)
	serviceSource: Optional[SecurityServiceSource | str] = Field(alias="serviceSource",default=None,)
	severity: Optional[SecurityAlertSeverity | str] = Field(alias="severity",default=None,)
	status: Optional[SecurityAlertStatus | str] = Field(alias="status",default=None,)
	systemTags: Optional[list[str]] = Field(alias="systemTags",default=None,)
	tenantId: Optional[str] = Field(alias="tenantId",default=None,)
	threatDisplayName: Optional[str] = Field(alias="threatDisplayName",default=None,)
	threatFamilyName: Optional[str] = Field(alias="threatFamilyName",default=None,)
	title: Optional[str] = Field(alias="title",default=None,)

from .security_dictionary import SecurityDictionary
from .security_alert_classification import SecurityAlertClassification
from .security_alert_comment import SecurityAlertComment
from .security_detection_source import SecurityDetectionSource
from .security_alert_determination import SecurityAlertDetermination
from .security_alert_evidence import SecurityAlertEvidence
from .security_service_source import SecurityServiceSource
from .security_alert_severity import SecurityAlertSeverity
from .security_alert_status import SecurityAlertStatus

