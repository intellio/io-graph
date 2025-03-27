from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class OneDriveForBusinessRestoreSession(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.oneDriveForBusinessRestoreSession"] = Field(alias="@odata.type", default="#microsoft.graph.oneDriveForBusinessRestoreSession")
	completedDateTime: Optional[datetime] = Field(alias="completedDateTime", default=None,)
	createdBy: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="createdBy", default=None,discriminator="odata_type", )
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	error: Optional[PublicError] = Field(alias="error", default=None,)
	lastModifiedBy: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="lastModifiedBy", default=None,discriminator="odata_type", )
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	restoreJobType: Optional[RestoreJobType | str] = Field(alias="restoreJobType", default=None,)
	restoreSessionArtifactCount: Optional[RestoreSessionArtifactCount] = Field(alias="restoreSessionArtifactCount", default=None,)
	status: Optional[RestoreSessionStatus | str] = Field(alias="status", default=None,)
	driveRestoreArtifacts: Optional[list[DriveRestoreArtifact]] = Field(alias="driveRestoreArtifacts", default=None,)
	driveRestoreArtifactsBulkAdditionRequests: Optional[list[DriveRestoreArtifactsBulkAdditionRequest]] = Field(alias="driveRestoreArtifactsBulkAdditionRequests", default=None,)

from .ai_interaction_mentioned_identity_set import AiInteractionMentionedIdentitySet
from .approval_identity_set import ApprovalIdentitySet
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .public_error import PublicError
from .ai_interaction_mentioned_identity_set import AiInteractionMentionedIdentitySet
from .approval_identity_set import ApprovalIdentitySet
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .restore_job_type import RestoreJobType
from .restore_session_artifact_count import RestoreSessionArtifactCount
from .restore_session_status import RestoreSessionStatus
from .drive_restore_artifact import DriveRestoreArtifact
from .drive_restore_artifacts_bulk_addition_request import DriveRestoreArtifactsBulkAdditionRequest

