from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ManagedAppPolicyDeploymentSummaryPerAppCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[ManagedAppPolicyDeploymentSummaryPerApp]] = Field(alias="value", default=None,)

from .managed_app_policy_deployment_summary_per_app import ManagedAppPolicyDeploymentSummaryPerApp
