from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AppliedConditionalAccessPolicy(BaseModel):
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	enforcedGrantControls: Optional[list[str]] = Field(default=None,alias="enforcedGrantControls",)
	enforcedSessionControls: Optional[list[str]] = Field(default=None,alias="enforcedSessionControls",)
	id: Optional[str] = Field(default=None,alias="id",)
	result: Optional[AppliedConditionalAccessPolicyResult] = Field(default=None,alias="result",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .applied_conditional_access_policy_result import AppliedConditionalAccessPolicyResult

