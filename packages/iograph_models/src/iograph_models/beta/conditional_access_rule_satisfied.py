from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ConditionalAccessRuleSatisfied(BaseModel):
	conditionalAccessCondition: Optional[ConditionalAccessConditions | str] = Field(alias="conditionalAccessCondition", default=None,)
	ruleSatisfied: Optional[ConditionalAccessRule | str] = Field(alias="ruleSatisfied", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .conditional_access_conditions import ConditionalAccessConditions
from .conditional_access_rule import ConditionalAccessRule

