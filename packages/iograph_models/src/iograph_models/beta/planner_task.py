from __future__ import annotations
from typing import Optional
from typing import Union
from datetime import datetime
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class PlannerTask(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	activeChecklistItemCount: Optional[int] = Field(alias="activeChecklistItemCount", default=None,)
	appliedCategories: Optional[PlannerAppliedCategories] = Field(alias="appliedCategories", default=None,)
	archivalInfo: Optional[PlannerArchivalInfo] = Field(alias="archivalInfo", default=None,)
	assigneePriority: Optional[str] = Field(alias="assigneePriority", default=None,)
	assignments: Optional[PlannerAssignments] = Field(alias="assignments", default=None,)
	bucketId: Optional[str] = Field(alias="bucketId", default=None,)
	checklistItemCount: Optional[int] = Field(alias="checklistItemCount", default=None,)
	completedBy: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="completedBy", default=None,discriminator="odata_type", )
	completedDateTime: Optional[datetime] = Field(alias="completedDateTime", default=None,)
	conversationThreadId: Optional[str] = Field(alias="conversationThreadId", default=None,)
	createdBy: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="createdBy", default=None,discriminator="odata_type", )
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	creationSource: Optional[Union[PlannerExternalTaskSource, PlannerTeamsPublicationInfo]] = Field(alias="creationSource", default=None,discriminator="odata_type", )
	dueDateTime: Optional[datetime] = Field(alias="dueDateTime", default=None,)
	hasDescription: Optional[bool] = Field(alias="hasDescription", default=None,)
	isArchived: Optional[bool] = Field(alias="isArchived", default=None,)
	isOnMyDay: Optional[bool] = Field(alias="isOnMyDay", default=None,)
	isOnMyDayLastModifiedDate: Optional[str] = Field(alias="isOnMyDayLastModifiedDate", default=None,)
	lastModifiedBy: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="lastModifiedBy", default=None,discriminator="odata_type", )
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	orderHint: Optional[str] = Field(alias="orderHint", default=None,)
	percentComplete: Optional[int] = Field(alias="percentComplete", default=None,)
	planId: Optional[str] = Field(alias="planId", default=None,)
	previewType: Optional[PlannerPreviewType | str] = Field(alias="previewType", default=None,)
	priority: Optional[int] = Field(alias="priority", default=None,)
	recurrence: Optional[PlannerTaskRecurrence] = Field(alias="recurrence", default=None,)
	referenceCount: Optional[int] = Field(alias="referenceCount", default=None,)
	specifiedCompletionRequirements: Optional[PlannerTaskCompletionRequirements | str] = Field(alias="specifiedCompletionRequirements", default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime", default=None,)
	title: Optional[str] = Field(alias="title", default=None,)
	assignedToTaskBoardFormat: Optional[PlannerAssignedToTaskBoardTaskFormat] = Field(alias="assignedToTaskBoardFormat", default=None,)
	bucketTaskBoardFormat: Optional[PlannerBucketTaskBoardTaskFormat] = Field(alias="bucketTaskBoardFormat", default=None,)
	details: Optional[PlannerTaskDetails] = Field(alias="details", default=None,)
	progressTaskBoardFormat: Optional[PlannerProgressTaskBoardTaskFormat] = Field(alias="progressTaskBoardFormat", default=None,)

	@model_validator(mode="wrap")
	def convert_discriminator_class(cls, data: Any, handler: ModelWrapValidatorHandler[Self]) -> Self:
		try:
			# check with parent model to catch any errors
			parent_validated_model = handler(data)
			# check if the discriminator field is present
			if "@odata.type" not in data:
				return parent_validated_model
			# get the discriminator value
			mapping_key = data["@odata.type"]
			if mapping_key == "#microsoft.graph.businessScenarioTask":
				from .business_scenario_task import BusinessScenarioTask
				return BusinessScenarioTask.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .planner_applied_categories import PlannerAppliedCategories
from .planner_archival_info import PlannerArchivalInfo
from .planner_assignments import PlannerAssignments
from .ai_interaction_mentioned_identity_set import AiInteractionMentionedIdentitySet
from .approval_identity_set import ApprovalIdentitySet
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .planner_external_task_source import PlannerExternalTaskSource
from .planner_teams_publication_info import PlannerTeamsPublicationInfo
from .planner_preview_type import PlannerPreviewType
from .planner_task_recurrence import PlannerTaskRecurrence
from .planner_task_completion_requirements import PlannerTaskCompletionRequirements
from .planner_assigned_to_task_board_task_format import PlannerAssignedToTaskBoardTaskFormat
from .planner_bucket_task_board_task_format import PlannerBucketTaskBoardTaskFormat
from .planner_task_details import PlannerTaskDetails
from .planner_progress_task_board_task_format import PlannerProgressTaskBoardTaskFormat
