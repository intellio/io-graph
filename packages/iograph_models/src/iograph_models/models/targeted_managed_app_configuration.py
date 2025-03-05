from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class TargetedManagedAppConfiguration(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	version: Optional[str] = Field(default=None,alias="version",)
	customSettings: Optional[list[KeyValuePair]] = Field(default=None,alias="customSettings",)
	deployedAppCount: Optional[int] = Field(default=None,alias="deployedAppCount",)
	isAssigned: Optional[bool] = Field(default=None,alias="isAssigned",)
	apps: Optional[list[ManagedMobileApp]] = Field(default=None,alias="apps",)
	assignments: Optional[list[TargetedManagedAppPolicyAssignment]] = Field(default=None,alias="assignments",)
	deploymentSummary: Optional[ManagedAppPolicyDeploymentSummary] = Field(default=None,alias="deploymentSummary",)

from .key_value_pair import KeyValuePair
from .managed_mobile_app import ManagedMobileApp
from .targeted_managed_app_policy_assignment import TargetedManagedAppPolicyAssignment
from .managed_app_policy_deployment_summary import ManagedAppPolicyDeploymentSummary

