from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ExchangeProtectionPolicy(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	retentionSettings: Optional[list[RetentionSetting]] = Field(alias="retentionSettings",default=None,)
	status: Optional[ProtectionPolicyStatus | str] = Field(alias="status",default=None,)
	mailboxInclusionRules: Optional[list[MailboxProtectionRule]] = Field(alias="mailboxInclusionRules",default=None,)
	mailboxProtectionUnits: Optional[list[MailboxProtectionUnit]] = Field(alias="mailboxProtectionUnits",default=None,)

from .identity_set import IdentitySet
from .identity_set import IdentitySet
from .retention_setting import RetentionSetting
from .protection_policy_status import ProtectionPolicyStatus
from .mailbox_protection_rule import MailboxProtectionRule
from .mailbox_protection_unit import MailboxProtectionUnit

