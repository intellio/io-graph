from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class SecurityBaselineState(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.securityBaselineState"] = Field(alias="@odata.type",)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	securityBaselineTemplateId: Optional[str] = Field(alias="securityBaselineTemplateId", default=None,)
	state: Optional[SecurityBaselineComplianceState | str] = Field(alias="state", default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName", default=None,)
	settingStates: Optional[list[SecurityBaselineSettingState]] = Field(alias="settingStates", default=None,)

from .security_baseline_compliance_state import SecurityBaselineComplianceState
from .security_baseline_setting_state import SecurityBaselineSettingState
