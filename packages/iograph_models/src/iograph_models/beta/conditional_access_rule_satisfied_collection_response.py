from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ConditionalAccessRuleSatisfiedCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[ConditionalAccessRuleSatisfied]] = Field(alias="value",default=None,)

from .conditional_access_rule_satisfied import ConditionalAccessRuleSatisfied

