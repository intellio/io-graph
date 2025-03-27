from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ConditionalAccessPolicyDetail(BaseModel):
	conditions: Optional[ConditionalAccessConditionSet] = Field(alias="conditions", default=None,)
	grantControls: Optional[ConditionalAccessGrantControls] = Field(alias="grantControls", default=None,)
	sessionControls: Optional[ConditionalAccessSessionControls] = Field(alias="sessionControls", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .conditional_access_condition_set import ConditionalAccessConditionSet
from .conditional_access_grant_controls import ConditionalAccessGrantControls
from .conditional_access_session_controls import ConditionalAccessSessionControls

