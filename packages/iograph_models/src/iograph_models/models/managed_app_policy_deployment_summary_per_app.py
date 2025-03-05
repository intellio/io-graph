from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ManagedAppPolicyDeploymentSummaryPerApp(BaseModel):
	configurationAppliedUserCount: Optional[int] = Field(default=None,alias="configurationAppliedUserCount",)
	mobileAppIdentifier: SerializeAsAny[Optional[MobileAppIdentifier]] = Field(default=None,alias="mobileAppIdentifier",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .mobile_app_identifier import MobileAppIdentifier

