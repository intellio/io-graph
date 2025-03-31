from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityRetentionLabel(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.security.retentionLabel"] = Field(alias="@odata.type",)
	actionAfterRetentionPeriod: Optional[SecurityActionAfterRetentionPeriod | str] = Field(alias="actionAfterRetentionPeriod", default=None,)
	behaviorDuringRetentionPeriod: Optional[SecurityBehaviorDuringRetentionPeriod | str] = Field(alias="behaviorDuringRetentionPeriod", default=None,)
	createdBy: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="createdBy", default=None,discriminator="odata_type", )
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	defaultRecordBehavior: Optional[SecurityDefaultRecordBehavior | str] = Field(alias="defaultRecordBehavior", default=None,)
	descriptionForAdmins: Optional[str] = Field(alias="descriptionForAdmins", default=None,)
	descriptionForUsers: Optional[str] = Field(alias="descriptionForUsers", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	isInUse: Optional[bool] = Field(alias="isInUse", default=None,)
	labelToBeApplied: Optional[str] = Field(alias="labelToBeApplied", default=None,)
	lastModifiedBy: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="lastModifiedBy", default=None,discriminator="odata_type", )
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	retentionDuration: Optional[Union[SecurityRetentionDurationForever, SecurityRetentionDurationInDays]] = Field(alias="retentionDuration", default=None,discriminator="odata_type", )
	retentionTrigger: Optional[SecurityRetentionTrigger | str] = Field(alias="retentionTrigger", default=None,)
	descriptors: Optional[SecurityFilePlanDescriptor] = Field(alias="descriptors", default=None,)
	dispositionReviewStages: Optional[list[SecurityDispositionReviewStage]] = Field(alias="dispositionReviewStages", default=None,)
	retentionEventType: Optional[SecurityRetentionEventType] = Field(alias="retentionEventType", default=None,)

from .security_action_after_retention_period import SecurityActionAfterRetentionPeriod
from .security_behavior_during_retention_period import SecurityBehaviorDuringRetentionPeriod
from .ai_interaction_mentioned_identity_set import AiInteractionMentionedIdentitySet
from .approval_identity_set import ApprovalIdentitySet
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .security_default_record_behavior import SecurityDefaultRecordBehavior
from .security_retention_duration_forever import SecurityRetentionDurationForever
from .security_retention_duration_in_days import SecurityRetentionDurationInDays
from .security_retention_trigger import SecurityRetentionTrigger
from .security_file_plan_descriptor import SecurityFilePlanDescriptor
from .security_disposition_review_stage import SecurityDispositionReviewStage
from .security_retention_event_type import SecurityRetentionEventType
