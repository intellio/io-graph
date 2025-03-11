from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class GovernanceRuleSettingCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[GovernanceRuleSetting]] = Field(alias="value",default=None,)

from .governance_rule_setting import GovernanceRuleSetting

