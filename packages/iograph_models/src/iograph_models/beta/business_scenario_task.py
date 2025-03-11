from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class BusinessScenarioTask(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	activeChecklistItemCount: Optional[int] = Field(alias="activeChecklistItemCount",default=None,)
	appliedCategories: Optional[PlannerAppliedCategories] = Field(alias="appliedCategories",default=None,)
	archivalInfo: Optional[PlannerArchivalInfo] = Field(alias="archivalInfo",default=None,)
	assigneePriority: Optional[str] = Field(alias="assigneePriority",default=None,)
	assignments: Optional[PlannerAssignments] = Field(alias="assignments",default=None,)
	bucketId: Optional[str] = Field(alias="bucketId",default=None,)
	checklistItemCount: Optional[int] = Field(alias="checklistItemCount",default=None,)
	completedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="completedBy",default=None,)
	completedDateTime: Optional[datetime] = Field(alias="completedDateTime",default=None,)
	conversationThreadId: Optional[str] = Field(alias="conversationThreadId",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	creationSource: SerializeAsAny[Optional[PlannerTaskCreation]] = Field(alias="creationSource",default=None,)
	dueDateTime: Optional[datetime] = Field(alias="dueDateTime",default=None,)
	hasDescription: Optional[bool] = Field(alias="hasDescription",default=None,)
	isArchived: Optional[bool] = Field(alias="isArchived",default=None,)
	isOnMyDay: Optional[bool] = Field(alias="isOnMyDay",default=None,)
	isOnMyDayLastModifiedDate: Optional[str] = Field(alias="isOnMyDayLastModifiedDate",default=None,)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	orderHint: Optional[str] = Field(alias="orderHint",default=None,)
	percentComplete: Optional[int] = Field(alias="percentComplete",default=None,)
	planId: Optional[str] = Field(alias="planId",default=None,)
	previewType: Optional[PlannerPreviewType | str] = Field(alias="previewType",default=None,)
	priority: Optional[int] = Field(alias="priority",default=None,)
	recurrence: Optional[PlannerTaskRecurrence] = Field(alias="recurrence",default=None,)
	referenceCount: Optional[int] = Field(alias="referenceCount",default=None,)
	specifiedCompletionRequirements: Optional[PlannerTaskCompletionRequirements | str] = Field(alias="specifiedCompletionRequirements",default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime",default=None,)
	title: Optional[str] = Field(alias="title",default=None,)
	assignedToTaskBoardFormat: Optional[PlannerAssignedToTaskBoardTaskFormat] = Field(alias="assignedToTaskBoardFormat",default=None,)
	bucketTaskBoardFormat: Optional[PlannerBucketTaskBoardTaskFormat] = Field(alias="bucketTaskBoardFormat",default=None,)
	details: Optional[PlannerTaskDetails] = Field(alias="details",default=None,)
	progressTaskBoardFormat: Optional[PlannerProgressTaskBoardTaskFormat] = Field(alias="progressTaskBoardFormat",default=None,)
	businessScenarioProperties: Optional[BusinessScenarioProperties] = Field(alias="businessScenarioProperties",default=None,)
	target: SerializeAsAny[Optional[BusinessScenarioTaskTargetBase]] = Field(alias="target",default=None,)

from .planner_applied_categories import PlannerAppliedCategories
from .planner_archival_info import PlannerArchivalInfo
from .planner_assignments import PlannerAssignments
from .identity_set import IdentitySet
from .identity_set import IdentitySet
from .planner_task_creation import PlannerTaskCreation
from .identity_set import IdentitySet
from .planner_preview_type import PlannerPreviewType
from .planner_task_recurrence import PlannerTaskRecurrence
from .planner_task_completion_requirements import PlannerTaskCompletionRequirements
from .planner_assigned_to_task_board_task_format import PlannerAssignedToTaskBoardTaskFormat
from .planner_bucket_task_board_task_format import PlannerBucketTaskBoardTaskFormat
from .planner_task_details import PlannerTaskDetails
from .planner_progress_task_board_task_format import PlannerProgressTaskBoardTaskFormat
from .business_scenario_properties import BusinessScenarioProperties
from .business_scenario_task_target_base import BusinessScenarioTaskTargetBase

