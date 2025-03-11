from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IdentityGovernanceRuleBasedSubjectSet(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	rule: Optional[str] = Field(alias="rule",default=None,)


