from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityServicePrincipalEvidence(BaseModel):
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	detailedRoles: Optional[list[str]] = Field(alias="detailedRoles",default=None,)
	remediationStatus: Optional[str | SecurityEvidenceRemediationStatus] = Field(alias="remediationStatus",default=None,)
	remediationStatusDetails: Optional[str] = Field(alias="remediationStatusDetails",default=None,)
	roles: Optional[list[str | SecurityEvidenceRole]] = Field(alias="roles",default=None,)
	tags: Optional[list[str]] = Field(alias="tags",default=None,)
	verdict: Optional[str | SecurityEvidenceVerdict] = Field(alias="verdict",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	appId: Optional[str] = Field(alias="appId",default=None,)
	appOwnerTenantId: Optional[str] = Field(alias="appOwnerTenantId",default=None,)
	servicePrincipalName: Optional[str] = Field(alias="servicePrincipalName",default=None,)
	servicePrincipalObjectId: Optional[str] = Field(alias="servicePrincipalObjectId",default=None,)
	servicePrincipalType: Optional[str | SecurityServicePrincipalType] = Field(alias="servicePrincipalType",default=None,)
	tenantId: Optional[str] = Field(alias="tenantId",default=None,)

from .security_evidence_remediation_status import SecurityEvidenceRemediationStatus
from .security_evidence_role import SecurityEvidenceRole
from .security_evidence_verdict import SecurityEvidenceVerdict
from .security_service_principal_type import SecurityServicePrincipalType

