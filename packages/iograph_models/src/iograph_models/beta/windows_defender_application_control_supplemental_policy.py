from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsDefenderApplicationControlSupplementalPolicy(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	content: Optional[str] = Field(alias="content", default=None,)
	contentFileName: Optional[str] = Field(alias="contentFileName", default=None,)
	creationDateTime: Optional[datetime] = Field(alias="creationDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	roleScopeTagIds: Optional[list[str]] = Field(alias="roleScopeTagIds", default=None,)
	version: Optional[str] = Field(alias="version", default=None,)
	assignments: Optional[list[WindowsDefenderApplicationControlSupplementalPolicyAssignment]] = Field(alias="assignments", default=None,)
	deploySummary: Optional[WindowsDefenderApplicationControlSupplementalPolicyDeploymentSummary] = Field(alias="deploySummary", default=None,)
	deviceStatuses: Optional[list[WindowsDefenderApplicationControlSupplementalPolicyDeploymentStatus]] = Field(alias="deviceStatuses", default=None,)

from .windows_defender_application_control_supplemental_policy_assignment import WindowsDefenderApplicationControlSupplementalPolicyAssignment
from .windows_defender_application_control_supplemental_policy_deployment_summary import WindowsDefenderApplicationControlSupplementalPolicyDeploymentSummary
from .windows_defender_application_control_supplemental_policy_deployment_status import WindowsDefenderApplicationControlSupplementalPolicyDeploymentStatus

