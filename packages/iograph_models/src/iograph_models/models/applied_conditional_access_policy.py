from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AppliedConditionalAccessPolicy(BaseModel):
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	enforcedGrantControls: Optional[list[str]] = Field(alias="enforcedGrantControls",default=None,)
	enforcedSessionControls: Optional[list[str]] = Field(alias="enforcedSessionControls",default=None,)
	id: Optional[str] = Field(alias="id",default=None,)
	result: Optional[AppliedConditionalAccessPolicyResult | str] = Field(alias="result",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .applied_conditional_access_policy_result import AppliedConditionalAccessPolicyResult

