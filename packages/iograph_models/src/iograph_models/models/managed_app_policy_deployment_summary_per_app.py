from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ManagedAppPolicyDeploymentSummaryPerApp(BaseModel):
	configurationAppliedUserCount: Optional[int] = Field(alias="configurationAppliedUserCount",default=None,)
	mobileAppIdentifier: SerializeAsAny[Optional[MobileAppIdentifier]] = Field(alias="mobileAppIdentifier",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .mobile_app_identifier import MobileAppIdentifier

