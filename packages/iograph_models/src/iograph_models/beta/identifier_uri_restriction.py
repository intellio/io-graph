from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class IdentifierUriRestriction(BaseModel):
	excludeActors: Optional[AppManagementPolicyActorExemptions] = Field(alias="excludeActors",default=None,)
	excludeAppsReceivingV2Tokens: Optional[bool] = Field(alias="excludeAppsReceivingV2Tokens",default=None,)
	excludeSaml: Optional[bool] = Field(alias="excludeSaml",default=None,)
	isStateSetByMicrosoft: Optional[bool] = Field(alias="isStateSetByMicrosoft",default=None,)
	restrictForAppsCreatedAfterDateTime: Optional[datetime] = Field(alias="restrictForAppsCreatedAfterDateTime",default=None,)
	state: Optional[AppManagementRestrictionState | str] = Field(alias="state",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .app_management_policy_actor_exemptions import AppManagementPolicyActorExemptions
from .app_management_restriction_state import AppManagementRestrictionState

