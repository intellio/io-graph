from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class EducationFeedbackResourceOutcome(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.educationFeedbackResourceOutcome"] = Field(alias="@odata.type", default="#microsoft.graph.educationFeedbackResourceOutcome")
	lastModifiedBy: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="lastModifiedBy", default=None,discriminator="odata_type", )
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	feedbackResource: Optional[Union[EducationChannelResource, EducationExcelResource, EducationExternalResource, EducationFileResource, EducationLinkedAssignmentResource, EducationLinkResource, EducationMediaResource, EducationPowerPointResource, EducationTeamsAppResource, EducationWordResource]] = Field(alias="feedbackResource", default=None,discriminator="odata_type", )
	resourceStatus: Optional[EducationFeedbackResourceOutcomeStatus | str] = Field(alias="resourceStatus", default=None,)

from .ai_interaction_mentioned_identity_set import AiInteractionMentionedIdentitySet
from .approval_identity_set import ApprovalIdentitySet
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .education_channel_resource import EducationChannelResource
from .education_excel_resource import EducationExcelResource
from .education_external_resource import EducationExternalResource
from .education_file_resource import EducationFileResource
from .education_linked_assignment_resource import EducationLinkedAssignmentResource
from .education_link_resource import EducationLinkResource
from .education_media_resource import EducationMediaResource
from .education_power_point_resource import EducationPowerPointResource
from .education_teams_app_resource import EducationTeamsAppResource
from .education_word_resource import EducationWordResource
from .education_feedback_resource_outcome_status import EducationFeedbackResourceOutcomeStatus

