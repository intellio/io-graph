from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MatchingDlpRule(BaseModel):
	actions: SerializeAsAny[Optional[list[DlpActionInfo]]] = Field(alias="actions",default=None,)
	isMostRestrictive: Optional[bool] = Field(alias="isMostRestrictive",default=None,)
	policyId: Optional[str] = Field(alias="policyId",default=None,)
	policyName: Optional[str] = Field(alias="policyName",default=None,)
	priority: Optional[int] = Field(alias="priority",default=None,)
	ruleId: Optional[str] = Field(alias="ruleId",default=None,)
	ruleMode: Optional[RuleMode | str] = Field(alias="ruleMode",default=None,)
	ruleName: Optional[str] = Field(alias="ruleName",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .dlp_action_info import DlpActionInfo
from .rule_mode import RuleMode

