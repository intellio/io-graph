from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class ManagedAppPolicyDeploymentSummary(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.managedAppPolicyDeploymentSummary"] = Field(alias="@odata.type",)
	configurationDeployedUserCount: Optional[int] = Field(alias="configurationDeployedUserCount", default=None,)
	configurationDeploymentSummaryPerApp: Optional[list[ManagedAppPolicyDeploymentSummaryPerApp]] = Field(alias="configurationDeploymentSummaryPerApp", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	lastRefreshTime: Optional[datetime] = Field(alias="lastRefreshTime", default=None,)
	version: Optional[str] = Field(alias="version", default=None,)

from .managed_app_policy_deployment_summary_per_app import ManagedAppPolicyDeploymentSummaryPerApp
