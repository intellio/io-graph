from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class DriveProtectionRule(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	error: Optional[PublicError] = Field(alias="error",default=None,)
	isAutoApplyEnabled: Optional[bool] = Field(alias="isAutoApplyEnabled",default=None,)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	status: Optional[ProtectionRuleStatus | str] = Field(alias="status",default=None,)
	driveExpression: Optional[str] = Field(alias="driveExpression",default=None,)

from .identity_set import IdentitySet
from .public_error import PublicError
from .identity_set import IdentitySet
from .protection_rule_status import ProtectionRuleStatus

