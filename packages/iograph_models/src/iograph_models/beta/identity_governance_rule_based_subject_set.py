from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class IdentityGovernanceRuleBasedSubjectSet(BaseModel):
	odata_type: Literal["#microsoft.graph.identityGovernance.ruleBasedSubjectSet"] = Field(alias="@odata.type", default="#microsoft.graph.identityGovernance.ruleBasedSubjectSet")
	rule: Optional[str] = Field(alias="rule", default=None,)


