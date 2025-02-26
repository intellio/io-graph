from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class MailboxProtectionRule(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdBy: Optional[IdentitySet] = Field(default=None,alias="createdBy",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	error: Optional[PublicError] = Field(default=None,alias="error",)
	isAutoApplyEnabled: Optional[bool] = Field(default=None,alias="isAutoApplyEnabled",)
	lastModifiedBy: Optional[IdentitySet] = Field(default=None,alias="lastModifiedBy",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	status: Optional[ProtectionRuleStatus] = Field(default=None,alias="status",)
	mailboxExpression: Optional[str] = Field(default=None,alias="mailboxExpression",)

from .identity_set import IdentitySet
from .public_error import PublicError
from .identity_set import IdentitySet
from .protection_rule_status import ProtectionRuleStatus

