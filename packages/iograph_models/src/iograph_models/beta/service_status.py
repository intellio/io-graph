from __future__ import annotations
from typing import Optional
from typing import Union
from datetime import datetime
from pydantic import BaseModel, Field


class ServiceStatus(BaseModel):
	backupServiceConsumer: Optional[BackupServiceConsumer | str] = Field(alias="backupServiceConsumer", default=None,)
	disableReason: Optional[DisableReason | str] = Field(alias="disableReason", default=None,)
	gracePeriodDateTime: Optional[datetime] = Field(alias="gracePeriodDateTime", default=None,)
	lastModifiedBy: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="lastModifiedBy", default=None,discriminator="odata_type", )
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	restoreAllowedTillDateTime: Optional[datetime] = Field(alias="restoreAllowedTillDateTime", default=None,)
	status: Optional[BackupServiceStatus | str] = Field(alias="status", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .backup_service_consumer import BackupServiceConsumer
from .disable_reason import DisableReason
from .ai_interaction_mentioned_identity_set import AiInteractionMentionedIdentitySet
from .approval_identity_set import ApprovalIdentitySet
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .backup_service_status import BackupServiceStatus
