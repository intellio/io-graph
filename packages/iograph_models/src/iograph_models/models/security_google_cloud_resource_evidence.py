from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityGoogleCloudResourceEvidence(BaseModel):
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	detailedRoles: Optional[list[str]] = Field(default=None,alias="detailedRoles",)
	remediationStatus: Optional[SecurityEvidenceRemediationStatus] = Field(default=None,alias="remediationStatus",)
	remediationStatusDetails: Optional[str] = Field(default=None,alias="remediationStatusDetails",)
	roles: Optional[list[SecurityEvidenceRole]] = Field(default=None,alias="roles",)
	tags: Optional[list[str]] = Field(default=None,alias="tags",)
	verdict: Optional[SecurityEvidenceVerdict] = Field(default=None,alias="verdict",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	fullResourceName: Optional[str] = Field(default=None,alias="fullResourceName",)
	location: Optional[str] = Field(default=None,alias="location",)
	locationType: Optional[SecurityGoogleCloudLocationType] = Field(default=None,alias="locationType",)
	projectId: Optional[str] = Field(default=None,alias="projectId",)
	projectNumber: Optional[int] = Field(default=None,alias="projectNumber",)
	resourceName: Optional[str] = Field(default=None,alias="resourceName",)
	resourceType: Optional[str] = Field(default=None,alias="resourceType",)

from .security_evidence_remediation_status import SecurityEvidenceRemediationStatus
from .security_evidence_role import SecurityEvidenceRole
from .security_evidence_verdict import SecurityEvidenceVerdict
from .security_google_cloud_location_type import SecurityGoogleCloudLocationType

