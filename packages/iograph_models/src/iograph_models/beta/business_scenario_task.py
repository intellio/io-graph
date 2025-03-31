from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class BusinessScenarioTask(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.businessScenarioTask"] = Field(alias="@odata.type",)
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
	businessScenarioProperties: Optional[BusinessScenarioProperties] = Field(alias="businessScenarioProperties", default=None,)
	target: Optional[Union[BusinessScenarioGroupTarget]] = Field(alias="target", default=None,discriminator="odata_type", )

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
from .business_scenario_properties import BusinessScenarioProperties
from .business_scenario_group_target import BusinessScenarioGroupTarget
