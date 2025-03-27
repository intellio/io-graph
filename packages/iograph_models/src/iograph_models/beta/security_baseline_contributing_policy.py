from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityBaselineContributingPolicy(BaseModel):
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	sourceId: Optional[str] = Field(alias="sourceId", default=None,)
	sourceType: Optional[SecurityBaselinePolicySourceType | str] = Field(alias="sourceType", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .security_baseline_policy_source_type import SecurityBaselinePolicySourceType

