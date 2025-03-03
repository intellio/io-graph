from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class ManagedAppPolicyDeploymentSummary(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	configurationDeployedUserCount: Optional[int] = Field(default=None,alias="configurationDeployedUserCount",)
	configurationDeploymentSummaryPerApp: Optional[list[ManagedAppPolicyDeploymentSummaryPerApp]] = Field(default=None,alias="configurationDeploymentSummaryPerApp",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	lastRefreshTime: Optional[datetime] = Field(default=None,alias="lastRefreshTime",)
	version: Optional[str] = Field(default=None,alias="version",)

from .managed_app_policy_deployment_summary_per_app import ManagedAppPolicyDeploymentSummaryPerApp

