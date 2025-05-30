from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class ConditionalAccessPolicy(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.conditionalAccessPolicy"] = Field(alias="@odata.type", default="#microsoft.graph.conditionalAccessPolicy")
	conditions: Optional[ConditionalAccessConditionSet] = Field(alias="conditions", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	grantControls: Optional[ConditionalAccessGrantControls] = Field(alias="grantControls", default=None,)
	modifiedDateTime: Optional[datetime] = Field(alias="modifiedDateTime", default=None,)
	sessionControls: Optional[ConditionalAccessSessionControls] = Field(alias="sessionControls", default=None,)
	state: Optional[ConditionalAccessPolicyState | str] = Field(alias="state", default=None,)
	templateId: Optional[str] = Field(alias="templateId", default=None,)

from .conditional_access_condition_set import ConditionalAccessConditionSet
from .conditional_access_grant_controls import ConditionalAccessGrantControls
from .conditional_access_session_controls import ConditionalAccessSessionControls
from .conditional_access_policy_state import ConditionalAccessPolicyState
