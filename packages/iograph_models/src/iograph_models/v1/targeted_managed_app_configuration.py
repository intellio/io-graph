from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class TargetedManagedAppConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.targetedManagedAppConfiguration"] = Field(alias="@odata.type", default="#microsoft.graph.targetedManagedAppConfiguration")
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	version: Optional[str] = Field(alias="version", default=None,)
	customSettings: Optional[list[KeyValuePair]] = Field(alias="customSettings", default=None,)
	deployedAppCount: Optional[int] = Field(alias="deployedAppCount", default=None,)
	isAssigned: Optional[bool] = Field(alias="isAssigned", default=None,)
	apps: Optional[list[ManagedMobileApp]] = Field(alias="apps", default=None,)
	assignments: Optional[list[TargetedManagedAppPolicyAssignment]] = Field(alias="assignments", default=None,)
	deploymentSummary: Optional[ManagedAppPolicyDeploymentSummary] = Field(alias="deploymentSummary", default=None,)

from .key_value_pair import KeyValuePair
from .managed_mobile_app import ManagedMobileApp
from .targeted_managed_app_policy_assignment import TargetedManagedAppPolicyAssignment
from .managed_app_policy_deployment_summary import ManagedAppPolicyDeploymentSummary
