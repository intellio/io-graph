from __future__ import annotations
from typing import Optional
from typing import Union
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SubjectRightsRequestHistory(BaseModel):
	changedBy: Optional[Union[ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="changedBy", default=None,discriminator="odata_type", )
	eventDateTime: Optional[datetime] = Field(alias="eventDateTime", default=None,)
	stage: Optional[SubjectRightsRequestStage | str] = Field(alias="stage", default=None,)
	stageStatus: Optional[SubjectRightsRequestStageStatus | str] = Field(alias="stageStatus", default=None,)
	type: Optional[str] = Field(alias="type", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .subject_rights_request_stage import SubjectRightsRequestStage
from .subject_rights_request_stage_status import SubjectRightsRequestStageStatus

