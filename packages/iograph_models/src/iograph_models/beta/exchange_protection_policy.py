from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class ExchangeProtectionPolicy(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.exchangeProtectionPolicy"] = Field(alias="@odata.type", default="#microsoft.graph.exchangeProtectionPolicy")
	createdBy: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="createdBy", default=None,discriminator="odata_type", )
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	lastModifiedBy: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="lastModifiedBy", default=None,discriminator="odata_type", )
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	retentionSettings: Optional[list[RetentionSetting]] = Field(alias="retentionSettings", default=None,)
	status: Optional[ProtectionPolicyStatus | str] = Field(alias="status", default=None,)
	mailboxInclusionRules: Optional[list[MailboxProtectionRule]] = Field(alias="mailboxInclusionRules", default=None,)
	mailboxProtectionUnits: Optional[list[MailboxProtectionUnit]] = Field(alias="mailboxProtectionUnits", default=None,)
	mailboxProtectionUnitsBulkAdditionJobs: Optional[list[MailboxProtectionUnitsBulkAdditionJob]] = Field(alias="mailboxProtectionUnitsBulkAdditionJobs", default=None,)

from .ai_interaction_mentioned_identity_set import AiInteractionMentionedIdentitySet
from .approval_identity_set import ApprovalIdentitySet
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .retention_setting import RetentionSetting
from .protection_policy_status import ProtectionPolicyStatus
from .mailbox_protection_rule import MailboxProtectionRule
from .mailbox_protection_unit import MailboxProtectionUnit
from .mailbox_protection_units_bulk_addition_job import MailboxProtectionUnitsBulkAdditionJob
