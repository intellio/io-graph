from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Windows10EnrollmentCompletionPageConfigurationPolicySetItem(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	errorCode: Optional[ErrorCode | str] = Field(alias="errorCode",default=None,)
	guidedDeploymentTags: Optional[list[str]] = Field(alias="guidedDeploymentTags",default=None,)
	itemType: Optional[str] = Field(alias="itemType",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	payloadId: Optional[str] = Field(alias="payloadId",default=None,)
	status: Optional[PolicySetStatus | str] = Field(alias="status",default=None,)
	priority: Optional[int] = Field(alias="priority",default=None,)

from .error_code import ErrorCode
from .policy_set_status import PolicySetStatus

