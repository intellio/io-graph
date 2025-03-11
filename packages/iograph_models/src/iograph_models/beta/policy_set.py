from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class PolicySet(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	errorCode: Optional[ErrorCode | str] = Field(alias="errorCode",default=None,)
	guidedDeploymentTags: Optional[list[str]] = Field(alias="guidedDeploymentTags",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	roleScopeTags: Optional[list[str]] = Field(alias="roleScopeTags",default=None,)
	status: Optional[PolicySetStatus | str] = Field(alias="status",default=None,)
	assignments: Optional[list[PolicySetAssignment]] = Field(alias="assignments",default=None,)
	items: SerializeAsAny[Optional[list[PolicySetItem]]] = Field(alias="items",default=None,)

from .error_code import ErrorCode
from .policy_set_status import PolicySetStatus
from .policy_set_assignment import PolicySetAssignment
from .policy_set_item import PolicySetItem

