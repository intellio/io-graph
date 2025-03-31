from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field


class EducationSubmission(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.educationSubmission"] = Field(alias="@odata.type",)
	assignmentId: Optional[str] = Field(alias="assignmentId", default=None,)
	excusedBy: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="excusedBy", default=None,discriminator="odata_type", )
	excusedDateTime: Optional[datetime] = Field(alias="excusedDateTime", default=None,)
	lastModifiedBy: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="lastModifiedBy", default=None,discriminator="odata_type", )
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	reassignedBy: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="reassignedBy", default=None,discriminator="odata_type", )
	reassignedDateTime: Optional[datetime] = Field(alias="reassignedDateTime", default=None,)
	recipient: Optional[Union[EducationSubmissionIndividualRecipient]] = Field(alias="recipient", default=None,discriminator="odata_type", )
	resourcesFolderUrl: Optional[str] = Field(alias="resourcesFolderUrl", default=None,)
	returnedBy: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="returnedBy", default=None,discriminator="odata_type", )
	returnedDateTime: Optional[datetime] = Field(alias="returnedDateTime", default=None,)
	status: Optional[EducationSubmissionStatus | str] = Field(alias="status", default=None,)
	submittedBy: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="submittedBy", default=None,discriminator="odata_type", )
	submittedDateTime: Optional[datetime] = Field(alias="submittedDateTime", default=None,)
	unsubmittedBy: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="unsubmittedBy", default=None,discriminator="odata_type", )
	unsubmittedDateTime: Optional[datetime] = Field(alias="unsubmittedDateTime", default=None,)
	webUrl: Optional[str] = Field(alias="webUrl", default=None,)
	outcomes: Optional[list[Annotated[Union[EducationFeedbackOutcome, EducationFeedbackResourceOutcome, EducationPointsOutcome, EducationRubricOutcome],Field(discriminator="odata_type")]]] = Field(alias="outcomes", default=None,)
	resources: Optional[list[EducationSubmissionResource]] = Field(alias="resources", default=None,)
	submittedResources: Optional[list[EducationSubmissionResource]] = Field(alias="submittedResources", default=None,)

from .ai_interaction_mentioned_identity_set import AiInteractionMentionedIdentitySet
from .approval_identity_set import ApprovalIdentitySet
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .education_submission_individual_recipient import EducationSubmissionIndividualRecipient
from .education_submission_status import EducationSubmissionStatus
from .education_feedback_outcome import EducationFeedbackOutcome
from .education_feedback_resource_outcome import EducationFeedbackResourceOutcome
from .education_points_outcome import EducationPointsOutcome
from .education_rubric_outcome import EducationRubricOutcome
from .education_submission_resource import EducationSubmissionResource
