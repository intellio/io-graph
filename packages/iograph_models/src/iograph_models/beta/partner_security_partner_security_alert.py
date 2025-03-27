from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class PartnerSecurityPartnerSecurityAlert(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	activityLogs: Optional[list[PartnerSecurityActivityLog]] = Field(alias="activityLogs", default=None,)
	additionalDetails: Optional[PartnerSecurityAdditionalDataDictionary] = Field(alias="additionalDetails", default=None,)
	affectedResources: Optional[list[PartnerSecurityAffectedResource]] = Field(alias="affectedResources", default=None,)
	alertType: Optional[str] = Field(alias="alertType", default=None,)
	catalogOfferId: Optional[str] = Field(alias="catalogOfferId", default=None,)
	confidenceLevel: Optional[PartnerSecuritySecurityAlertConfidence | str] = Field(alias="confidenceLevel", default=None,)
	customerTenantId: Optional[str] = Field(alias="customerTenantId", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	detectedDateTime: Optional[datetime] = Field(alias="detectedDateTime", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	firstObservedDateTime: Optional[datetime] = Field(alias="firstObservedDateTime", default=None,)
	isTest: Optional[bool] = Field(alias="isTest", default=None,)
	lastObservedDateTime: Optional[datetime] = Field(alias="lastObservedDateTime", default=None,)
	resolvedBy: Optional[str] = Field(alias="resolvedBy", default=None,)
	resolvedOnDateTime: Optional[datetime] = Field(alias="resolvedOnDateTime", default=None,)
	resolvedReason: Optional[PartnerSecuritySecurityAlertResolvedReason | str] = Field(alias="resolvedReason", default=None,)
	severity: Optional[PartnerSecuritySecurityAlertSeverity | str] = Field(alias="severity", default=None,)
	status: Optional[PartnerSecuritySecurityAlertStatus | str] = Field(alias="status", default=None,)
	subscriptionId: Optional[str] = Field(alias="subscriptionId", default=None,)
	valueAddedResellerTenantId: Optional[str] = Field(alias="valueAddedResellerTenantId", default=None,)

from .partner_security_activity_log import PartnerSecurityActivityLog
from .partner_security_additional_data_dictionary import PartnerSecurityAdditionalDataDictionary
from .partner_security_affected_resource import PartnerSecurityAffectedResource
from .partner_security_security_alert_confidence import PartnerSecuritySecurityAlertConfidence
from .partner_security_security_alert_resolved_reason import PartnerSecuritySecurityAlertResolvedReason
from .partner_security_security_alert_severity import PartnerSecuritySecurityAlertSeverity
from .partner_security_security_alert_status import PartnerSecuritySecurityAlertStatus

