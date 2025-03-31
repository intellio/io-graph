from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class EducationalActivity(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.educationalActivity"] = Field(alias="@odata.type", default="#microsoft.graph.educationalActivity")
	allowedAudiences: Optional[AllowedAudiences | str] = Field(alias="allowedAudiences", default=None,)
	createdBy: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="createdBy", default=None,discriminator="odata_type", )
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	inference: Optional[InferenceData] = Field(alias="inference", default=None,)
	isSearchable: Optional[bool] = Field(alias="isSearchable", default=None,)
	lastModifiedBy: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="lastModifiedBy", default=None,discriminator="odata_type", )
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	source: Optional[PersonDataSources] = Field(alias="source", default=None,)
	sources: Optional[list[ProfileSourceAnnotation]] = Field(alias="sources", default=None,)
	completionMonthYear: Optional[str] = Field(alias="completionMonthYear", default=None,)
	endMonthYear: Optional[str] = Field(alias="endMonthYear", default=None,)
	institution: Optional[InstitutionData] = Field(alias="institution", default=None,)
	program: Optional[EducationalActivityDetail] = Field(alias="program", default=None,)
	startMonthYear: Optional[str] = Field(alias="startMonthYear", default=None,)

from .allowed_audiences import AllowedAudiences
from .ai_interaction_mentioned_identity_set import AiInteractionMentionedIdentitySet
from .approval_identity_set import ApprovalIdentitySet
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .inference_data import InferenceData
from .person_data_sources import PersonDataSources
from .profile_source_annotation import ProfileSourceAnnotation
from .institution_data import InstitutionData
from .educational_activity_detail import EducationalActivityDetail
