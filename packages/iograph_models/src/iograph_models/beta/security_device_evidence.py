from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityDeviceEvidence(BaseModel):
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	detailedRoles: Optional[list[str]] = Field(alias="detailedRoles", default=None,)
	remediationStatus: Optional[SecurityEvidenceRemediationStatus | str] = Field(alias="remediationStatus", default=None,)
	remediationStatusDetails: Optional[str] = Field(alias="remediationStatusDetails", default=None,)
	roles: Optional[list[SecurityEvidenceRole | str]] = Field(alias="roles", default=None,)
	tags: Optional[list[str]] = Field(alias="tags", default=None,)
	verdict: Optional[SecurityEvidenceVerdict | str] = Field(alias="verdict", default=None,)
	odata_type: Literal["#microsoft.graph.security.deviceEvidence"] = Field(alias="@odata.type", default="#microsoft.graph.security.deviceEvidence")
	azureAdDeviceId: Optional[str] = Field(alias="azureAdDeviceId", default=None,)
	defenderAvStatus: Optional[SecurityDefenderAvStatus | str] = Field(alias="defenderAvStatus", default=None,)
	deviceDnsName: Optional[str] = Field(alias="deviceDnsName", default=None,)
	dnsDomain: Optional[str] = Field(alias="dnsDomain", default=None,)
	firstSeenDateTime: Optional[datetime] = Field(alias="firstSeenDateTime", default=None,)
	healthStatus: Optional[SecurityDeviceHealthStatus | str] = Field(alias="healthStatus", default=None,)
	hostName: Optional[str] = Field(alias="hostName", default=None,)
	ipInterfaces: Optional[list[str]] = Field(alias="ipInterfaces", default=None,)
	lastExternalIpAddress: Optional[str] = Field(alias="lastExternalIpAddress", default=None,)
	lastIpAddress: Optional[str] = Field(alias="lastIpAddress", default=None,)
	loggedOnUsers: Optional[list[SecurityLoggedOnUser]] = Field(alias="loggedOnUsers", default=None,)
	mdeDeviceId: Optional[str] = Field(alias="mdeDeviceId", default=None,)
	ntDomain: Optional[str] = Field(alias="ntDomain", default=None,)
	onboardingStatus: Optional[SecurityOnboardingStatus | str] = Field(alias="onboardingStatus", default=None,)
	osBuild: Optional[int] = Field(alias="osBuild", default=None,)
	osPlatform: Optional[str] = Field(alias="osPlatform", default=None,)
	rbacGroupId: Optional[int] = Field(alias="rbacGroupId", default=None,)
	rbacGroupName: Optional[str] = Field(alias="rbacGroupName", default=None,)
	riskScore: Optional[SecurityDeviceRiskScore | str] = Field(alias="riskScore", default=None,)
	version: Optional[str] = Field(alias="version", default=None,)
	vmMetadata: Optional[SecurityVmMetadata] = Field(alias="vmMetadata", default=None,)

from .security_evidence_remediation_status import SecurityEvidenceRemediationStatus
from .security_evidence_role import SecurityEvidenceRole
from .security_evidence_verdict import SecurityEvidenceVerdict
from .security_defender_av_status import SecurityDefenderAvStatus
from .security_device_health_status import SecurityDeviceHealthStatus
from .security_logged_on_user import SecurityLoggedOnUser
from .security_onboarding_status import SecurityOnboardingStatus
from .security_device_risk_score import SecurityDeviceRiskScore
from .security_vm_metadata import SecurityVmMetadata
