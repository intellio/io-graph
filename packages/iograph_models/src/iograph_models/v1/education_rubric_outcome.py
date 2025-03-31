from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class EducationRubricOutcome(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.educationRubricOutcome"] = Field(alias="@odata.type", default="#microsoft.graph.educationRubricOutcome")
	lastModifiedBy: Optional[Union[ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="lastModifiedBy", default=None,discriminator="odata_type", )
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	publishedRubricQualityFeedback: Optional[list[RubricQualityFeedbackModel]] = Field(alias="publishedRubricQualityFeedback", default=None,)
	publishedRubricQualitySelectedLevels: Optional[list[RubricQualitySelectedColumnModel]] = Field(alias="publishedRubricQualitySelectedLevels", default=None,)
	rubricQualityFeedback: Optional[list[RubricQualityFeedbackModel]] = Field(alias="rubricQualityFeedback", default=None,)
	rubricQualitySelectedLevels: Optional[list[RubricQualitySelectedColumnModel]] = Field(alias="rubricQualitySelectedLevels", default=None,)

from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .rubric_quality_feedback_model import RubricQualityFeedbackModel
from .rubric_quality_selected_column_model import RubricQualitySelectedColumnModel
