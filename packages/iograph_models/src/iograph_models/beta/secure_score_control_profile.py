from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecureScoreControlProfile(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	actionType: Optional[str] = Field(alias="actionType",default=None,)
	actionUrl: Optional[str] = Field(alias="actionUrl",default=None,)
	azureTenantId: Optional[str] = Field(alias="azureTenantId",default=None,)
	complianceInformation: Optional[list[ComplianceInformation]] = Field(alias="complianceInformation",default=None,)
	controlCategory: Optional[str] = Field(alias="controlCategory",default=None,)
	controlStateUpdates: Optional[list[SecureScoreControlStateUpdate]] = Field(alias="controlStateUpdates",default=None,)
	deprecated: Optional[bool] = Field(alias="deprecated",default=None,)
	implementationCost: Optional[str] = Field(alias="implementationCost",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	maxScore: float | str | ReferenceNumeric
	rank: Optional[int] = Field(alias="rank",default=None,)
	remediation: Optional[str] = Field(alias="remediation",default=None,)
	remediationImpact: Optional[str] = Field(alias="remediationImpact",default=None,)
	service: Optional[str] = Field(alias="service",default=None,)
	threats: Optional[list[str]] = Field(alias="threats",default=None,)
	tier: Optional[str] = Field(alias="tier",default=None,)
	title: Optional[str] = Field(alias="title",default=None,)
	userImpact: Optional[str] = Field(alias="userImpact",default=None,)
	vendorInformation: Optional[SecurityVendorInformation] = Field(alias="vendorInformation",default=None,)

from .compliance_information import ComplianceInformation
from .secure_score_control_state_update import SecureScoreControlStateUpdate
from .reference_numeric import ReferenceNumeric
from .security_vendor_information import SecurityVendorInformation

