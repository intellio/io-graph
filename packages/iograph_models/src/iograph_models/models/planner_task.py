from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class PlannerTask(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	activeChecklistItemCount: Optional[int] = Field(default=None,alias="activeChecklistItemCount",)
	appliedCategories: Optional[PlannerAppliedCategories] = Field(default=None,alias="appliedCategories",)
	assigneePriority: Optional[str] = Field(default=None,alias="assigneePriority",)
	assignments: Optional[PlannerAssignments] = Field(default=None,alias="assignments",)
	bucketId: Optional[str] = Field(default=None,alias="bucketId",)
	checklistItemCount: Optional[int] = Field(default=None,alias="checklistItemCount",)
	completedBy: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="completedBy",)
	completedDateTime: Optional[datetime] = Field(default=None,alias="completedDateTime",)
	conversationThreadId: Optional[str] = Field(default=None,alias="conversationThreadId",)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="createdBy",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	dueDateTime: Optional[datetime] = Field(default=None,alias="dueDateTime",)
	hasDescription: Optional[bool] = Field(default=None,alias="hasDescription",)
	orderHint: Optional[str] = Field(default=None,alias="orderHint",)
	percentComplete: Optional[int] = Field(default=None,alias="percentComplete",)
	planId: Optional[str] = Field(default=None,alias="planId",)
	previewType: Optional[PlannerPreviewType] = Field(default=None,alias="previewType",)
	priority: Optional[int] = Field(default=None,alias="priority",)
	referenceCount: Optional[int] = Field(default=None,alias="referenceCount",)
	startDateTime: Optional[datetime] = Field(default=None,alias="startDateTime",)
	title: Optional[str] = Field(default=None,alias="title",)
	assignedToTaskBoardFormat: Optional[PlannerAssignedToTaskBoardTaskFormat] = Field(default=None,alias="assignedToTaskBoardFormat",)
	bucketTaskBoardFormat: Optional[PlannerBucketTaskBoardTaskFormat] = Field(default=None,alias="bucketTaskBoardFormat",)
	details: Optional[PlannerTaskDetails] = Field(default=None,alias="details",)
	progressTaskBoardFormat: Optional[PlannerProgressTaskBoardTaskFormat] = Field(default=None,alias="progressTaskBoardFormat",)

from .planner_applied_categories import PlannerAppliedCategories
from .planner_assignments import PlannerAssignments
from .identity_set import IdentitySet
from .identity_set import IdentitySet
from .planner_preview_type import PlannerPreviewType
from .planner_assigned_to_task_board_task_format import PlannerAssignedToTaskBoardTaskFormat
from .planner_bucket_task_board_task_format import PlannerBucketTaskBoardTaskFormat
from .planner_task_details import PlannerTaskDetails
from .planner_progress_task_board_task_format import PlannerProgressTaskBoardTaskFormat

