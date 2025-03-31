from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class OpenShift(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.openShift"] = Field(alias="@odata.type", default="#microsoft.graph.openShift")
	createdBy: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="createdBy", default=None,discriminator="odata_type", )
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	lastModifiedBy: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="lastModifiedBy", default=None,discriminator="odata_type", )
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	draftOpenShift: Optional[OpenShiftItem] = Field(alias="draftOpenShift", default=None,)
	isStagedForDeletion: Optional[bool] = Field(alias="isStagedForDeletion", default=None,)
	schedulingGroupId: Optional[str] = Field(alias="schedulingGroupId", default=None,)
	schedulingGroupInfo: Optional[SchedulingGroupInfo] = Field(alias="schedulingGroupInfo", default=None,)
	sharedOpenShift: Optional[OpenShiftItem] = Field(alias="sharedOpenShift", default=None,)
	teamInfo: Optional[ShiftsTeamInfo] = Field(alias="teamInfo", default=None,)

from .ai_interaction_mentioned_identity_set import AiInteractionMentionedIdentitySet
from .approval_identity_set import ApprovalIdentitySet
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .open_shift_item import OpenShiftItem
from .scheduling_group_info import SchedulingGroupInfo
from .shifts_team_info import ShiftsTeamInfo
