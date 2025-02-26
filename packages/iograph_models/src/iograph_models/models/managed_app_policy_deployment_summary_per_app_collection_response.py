from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ManagedAppPolicyDeploymentSummaryPerAppCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[ManagedAppPolicyDeploymentSummaryPerApp] = Field(alias="value",)

from .managed_app_policy_deployment_summary_per_app import ManagedAppPolicyDeploymentSummaryPerApp

