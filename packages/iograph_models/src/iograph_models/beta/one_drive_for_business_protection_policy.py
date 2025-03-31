from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class OneDriveForBusinessProtectionPolicy(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.oneDriveForBusinessProtectionPolicy"] = Field(alias="@odata.type", default="#microsoft.graph.oneDriveForBusinessProtectionPolicy")
	createdBy: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="createdBy", default=None,discriminator="odata_type", )
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	lastModifiedBy: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="lastModifiedBy", default=None,discriminator="odata_type", )
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	retentionSettings: Optional[list[RetentionSetting]] = Field(alias="retentionSettings", default=None,)
	status: Optional[ProtectionPolicyStatus | str] = Field(alias="status", default=None,)
	driveInclusionRules: Optional[list[DriveProtectionRule]] = Field(alias="driveInclusionRules", default=None,)
	driveProtectionUnits: Optional[list[DriveProtectionUnit]] = Field(alias="driveProtectionUnits", default=None,)
	driveProtectionUnitsBulkAdditionJobs: Optional[list[DriveProtectionUnitsBulkAdditionJob]] = Field(alias="driveProtectionUnitsBulkAdditionJobs", default=None,)

from .ai_interaction_mentioned_identity_set import AiInteractionMentionedIdentitySet
from .approval_identity_set import ApprovalIdentitySet
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .retention_setting import RetentionSetting
from .protection_policy_status import ProtectionPolicyStatus
from .drive_protection_rule import DriveProtectionRule
from .drive_protection_unit import DriveProtectionUnit
from .drive_protection_units_bulk_addition_job import DriveProtectionUnitsBulkAdditionJob
