from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class TimeOff(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.timeOff"] = Field(alias="@odata.type", default="#microsoft.graph.timeOff")
	createdBy: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="createdBy", default=None,discriminator="odata_type", )
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	lastModifiedBy: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="lastModifiedBy", default=None,discriminator="odata_type", )
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	draftTimeOff: Optional[TimeOffItem] = Field(alias="draftTimeOff", default=None,)
	isStagedForDeletion: Optional[bool] = Field(alias="isStagedForDeletion", default=None,)
	sharedTimeOff: Optional[TimeOffItem] = Field(alias="sharedTimeOff", default=None,)
	teamInfo: Optional[ShiftsTeamInfo] = Field(alias="teamInfo", default=None,)
	userId: Optional[str] = Field(alias="userId", default=None,)
	userInfo: Optional[ShiftsUserInfo] = Field(alias="userInfo", default=None,)

from .ai_interaction_mentioned_identity_set import AiInteractionMentionedIdentitySet
from .approval_identity_set import ApprovalIdentitySet
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .time_off_item import TimeOffItem
from .shifts_team_info import ShiftsTeamInfo
from .shifts_user_info import ShiftsUserInfo
