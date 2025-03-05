from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecureScoreControlProfile(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	actionType: Optional[str] = Field(default=None,alias="actionType",)
	actionUrl: Optional[str] = Field(default=None,alias="actionUrl",)
	azureTenantId: Optional[str] = Field(default=None,alias="azureTenantId",)
	complianceInformation: Optional[list[ComplianceInformation]] = Field(default=None,alias="complianceInformation",)
	controlCategory: Optional[str] = Field(default=None,alias="controlCategory",)
	controlStateUpdates: Optional[list[SecureScoreControlStateUpdate]] = Field(default=None,alias="controlStateUpdates",)
	deprecated: Optional[bool] = Field(default=None,alias="deprecated",)
	implementationCost: Optional[str] = Field(default=None,alias="implementationCost",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	maxScore: float | str | ReferenceNumeric
	rank: Optional[int] = Field(default=None,alias="rank",)
	remediation: Optional[str] = Field(default=None,alias="remediation",)
	remediationImpact: Optional[str] = Field(default=None,alias="remediationImpact",)
	service: Optional[str] = Field(default=None,alias="service",)
	threats: Optional[list[str]] = Field(default=None,alias="threats",)
	tier: Optional[str] = Field(default=None,alias="tier",)
	title: Optional[str] = Field(default=None,alias="title",)
	userImpact: Optional[str] = Field(default=None,alias="userImpact",)
	vendorInformation: Optional[SecurityVendorInformation] = Field(default=None,alias="vendorInformation",)

from .compliance_information import ComplianceInformation
from .secure_score_control_state_update import SecureScoreControlStateUpdate
from .reference_numeric import ReferenceNumeric
from .security_vendor_information import SecurityVendorInformation

