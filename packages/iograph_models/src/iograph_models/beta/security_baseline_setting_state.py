from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityBaselineSettingState(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	contributingPolicies: Optional[list[SecurityBaselineContributingPolicy]] = Field(alias="contributingPolicies",default=None,)
	errorCode: Optional[str] = Field(alias="errorCode",default=None,)
	settingCategoryId: Optional[str] = Field(alias="settingCategoryId",default=None,)
	settingCategoryName: Optional[str] = Field(alias="settingCategoryName",default=None,)
	settingId: Optional[str] = Field(alias="settingId",default=None,)
	settingName: Optional[str] = Field(alias="settingName",default=None,)
	sourcePolicies: Optional[list[SettingSource]] = Field(alias="sourcePolicies",default=None,)
	state: Optional[SecurityBaselineComplianceState | str] = Field(alias="state",default=None,)

from .security_baseline_contributing_policy import SecurityBaselineContributingPolicy
from .setting_source import SettingSource
from .security_baseline_compliance_state import SecurityBaselineComplianceState

