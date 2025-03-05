from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ConditionalAccessPolicyDetail(BaseModel):
	conditions: Optional[ConditionalAccessConditionSet] = Field(default=None,alias="conditions",)
	grantControls: Optional[ConditionalAccessGrantControls] = Field(default=None,alias="grantControls",)
	sessionControls: Optional[ConditionalAccessSessionControls] = Field(default=None,alias="sessionControls",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .conditional_access_condition_set import ConditionalAccessConditionSet
from .conditional_access_grant_controls import ConditionalAccessGrantControls
from .conditional_access_session_controls import ConditionalAccessSessionControls

