from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class EducationAssignmentPointsGrade(BaseModel):
	gradedBy: Optional[Union[ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="gradedBy", default=None,discriminator="odata_type", )
	gradedDateTime: Optional[datetime] = Field(alias="gradedDateTime", default=None,)
	odata_type: Literal["#microsoft.graph.educationAssignmentPointsGrade"] = Field(alias="@odata.type", default="#microsoft.graph.educationAssignmentPointsGrade")
	points: float | str | ReferenceNumeric

from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .reference_numeric import ReferenceNumeric
