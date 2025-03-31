from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class MailboxRestoreArtifactsBulkAdditionRequest(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.mailboxRestoreArtifactsBulkAdditionRequest"] = Field(alias="@odata.type",)
	createdBy: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="createdBy", default=None,discriminator="odata_type", )
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	destinationType: Optional[DestinationType | str] = Field(alias="destinationType", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	error: Optional[PublicError] = Field(alias="error", default=None,)
	lastModifiedBy: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="lastModifiedBy", default=None,discriminator="odata_type", )
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	protectionTimePeriod: Optional[TimePeriod] = Field(alias="protectionTimePeriod", default=None,)
	protectionUnitIds: Optional[list[str]] = Field(alias="protectionUnitIds", default=None,)
	restorePointPreference: Optional[RestorePointPreference | str] = Field(alias="restorePointPreference", default=None,)
	status: Optional[RestoreArtifactsBulkRequestStatus | str] = Field(alias="status", default=None,)
	tags: Optional[RestorePointTags | str] = Field(alias="tags", default=None,)
	directoryObjectIds: Optional[list[str]] = Field(alias="directoryObjectIds", default=None,)
	mailboxes: Optional[list[str]] = Field(alias="mailboxes", default=None,)

from .ai_interaction_mentioned_identity_set import AiInteractionMentionedIdentitySet
from .approval_identity_set import ApprovalIdentitySet
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .destination_type import DestinationType
from .public_error import PublicError
from .time_period import TimePeriod
from .restore_point_preference import RestorePointPreference
from .restore_artifacts_bulk_request_status import RestoreArtifactsBulkRequestStatus
from .restore_point_tags import RestorePointTags
