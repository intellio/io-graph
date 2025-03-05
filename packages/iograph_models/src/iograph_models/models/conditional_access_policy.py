from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ConditionalAccessPolicy(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	conditions: Optional[ConditionalAccessConditionSet] = Field(default=None,alias="conditions",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	grantControls: Optional[ConditionalAccessGrantControls] = Field(default=None,alias="grantControls",)
	modifiedDateTime: Optional[datetime] = Field(default=None,alias="modifiedDateTime",)
	sessionControls: Optional[ConditionalAccessSessionControls] = Field(default=None,alias="sessionControls",)
	state: Optional[ConditionalAccessPolicyState] = Field(default=None,alias="state",)
	templateId: Optional[str] = Field(default=None,alias="templateId",)

from .conditional_access_condition_set import ConditionalAccessConditionSet
from .conditional_access_grant_controls import ConditionalAccessGrantControls
from .conditional_access_session_controls import ConditionalAccessSessionControls
from .conditional_access_policy_state import ConditionalAccessPolicyState

