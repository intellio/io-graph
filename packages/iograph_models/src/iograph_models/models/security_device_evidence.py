from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityDeviceEvidence(BaseModel):
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	detailedRoles: list[Optional[str]] = Field(alias="detailedRoles",)
	remediationStatus: Optional[SecurityEvidenceRemediationStatus] = Field(default=None,alias="remediationStatus",)
	remediationStatusDetails: Optional[str] = Field(default=None,alias="remediationStatusDetails",)
	roles: list[SecurityEvidenceRole] = Field(alias="roles",)
	tags: list[Optional[str]] = Field(alias="tags",)
	verdict: Optional[SecurityEvidenceVerdict] = Field(default=None,alias="verdict",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	azureAdDeviceId: Optional[str] = Field(default=None,alias="azureAdDeviceId",)
	defenderAvStatus: Optional[SecurityDefenderAvStatus] = Field(default=None,alias="defenderAvStatus",)
	deviceDnsName: Optional[str] = Field(default=None,alias="deviceDnsName",)
	dnsDomain: Optional[str] = Field(default=None,alias="dnsDomain",)
	firstSeenDateTime: Optional[datetime] = Field(default=None,alias="firstSeenDateTime",)
	healthStatus: Optional[SecurityDeviceHealthStatus] = Field(default=None,alias="healthStatus",)
	hostName: Optional[str] = Field(default=None,alias="hostName",)
	ipInterfaces: list[Optional[str]] = Field(alias="ipInterfaces",)
	lastExternalIpAddress: Optional[str] = Field(default=None,alias="lastExternalIpAddress",)
	lastIpAddress: Optional[str] = Field(default=None,alias="lastIpAddress",)
	loggedOnUsers: list[SecurityLoggedOnUser] = Field(alias="loggedOnUsers",)
	mdeDeviceId: Optional[str] = Field(default=None,alias="mdeDeviceId",)
	ntDomain: Optional[str] = Field(default=None,alias="ntDomain",)
	onboardingStatus: Optional[SecurityOnboardingStatus] = Field(default=None,alias="onboardingStatus",)
	osBuild: Optional[int] = Field(default=None,alias="osBuild",)
	osPlatform: Optional[str] = Field(default=None,alias="osPlatform",)
	rbacGroupId: Optional[int] = Field(default=None,alias="rbacGroupId",)
	rbacGroupName: Optional[str] = Field(default=None,alias="rbacGroupName",)
	riskScore: Optional[SecurityDeviceRiskScore] = Field(default=None,alias="riskScore",)
	version: Optional[str] = Field(default=None,alias="version",)
	vmMetadata: Optional[SecurityVmMetadata] = Field(default=None,alias="vmMetadata",)

from .security_evidence_remediation_status import SecurityEvidenceRemediationStatus
from .security_evidence_role import SecurityEvidenceRole
from .security_evidence_verdict import SecurityEvidenceVerdict
from .security_defender_av_status import SecurityDefenderAvStatus
from .security_device_health_status import SecurityDeviceHealthStatus
from .security_logged_on_user import SecurityLoggedOnUser
from .security_onboarding_status import SecurityOnboardingStatus
from .security_device_risk_score import SecurityDeviceRiskScore
from .security_vm_metadata import SecurityVmMetadata

