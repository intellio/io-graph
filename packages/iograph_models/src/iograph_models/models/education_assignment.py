from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class EducationAssignment(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	addedStudentAction: Optional[EducationAddedStudentAction] = Field(default=None,alias="addedStudentAction",)
	addToCalendarAction: Optional[EducationAddToCalendarOptions] = Field(default=None,alias="addToCalendarAction",)
	allowLateSubmissions: Optional[bool] = Field(default=None,alias="allowLateSubmissions",)
	allowStudentsToAddResourcesToSubmission: Optional[bool] = Field(default=None,alias="allowStudentsToAddResourcesToSubmission",)
	assignDateTime: Optional[datetime] = Field(default=None,alias="assignDateTime",)
	assignedDateTime: Optional[datetime] = Field(default=None,alias="assignedDateTime",)
	assignTo: Optional[EducationAssignmentRecipient] = Field(default=None,alias="assignTo",)
	classId: Optional[str] = Field(default=None,alias="classId",)
	closeDateTime: Optional[datetime] = Field(default=None,alias="closeDateTime",)
	createdBy: Optional[IdentitySet] = Field(default=None,alias="createdBy",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	dueDateTime: Optional[datetime] = Field(default=None,alias="dueDateTime",)
	feedbackResourcesFolderUrl: Optional[str] = Field(default=None,alias="feedbackResourcesFolderUrl",)
	grading: Optional[EducationAssignmentGradeType] = Field(default=None,alias="grading",)
	instructions: Optional[EducationItemBody] = Field(default=None,alias="instructions",)
	lastModifiedBy: Optional[IdentitySet] = Field(default=None,alias="lastModifiedBy",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	moduleUrl: Optional[str] = Field(default=None,alias="moduleUrl",)
	notificationChannelUrl: Optional[str] = Field(default=None,alias="notificationChannelUrl",)
	resourcesFolderUrl: Optional[str] = Field(default=None,alias="resourcesFolderUrl",)
	status: Optional[EducationAssignmentStatus] = Field(default=None,alias="status",)
	webUrl: Optional[str] = Field(default=None,alias="webUrl",)
	categories: Optional[list[EducationCategory]] = Field(default=None,alias="categories",)
	gradingCategory: Optional[EducationGradingCategory] = Field(default=None,alias="gradingCategory",)
	resources: Optional[list[EducationAssignmentResource]] = Field(default=None,alias="resources",)
	rubric: Optional[EducationRubric] = Field(default=None,alias="rubric",)
	submissions: Optional[list[EducationSubmission]] = Field(default=None,alias="submissions",)

from .education_added_student_action import EducationAddedStudentAction
from .education_add_to_calendar_options import EducationAddToCalendarOptions
from .education_assignment_recipient import EducationAssignmentRecipient
from .identity_set import IdentitySet
from .education_assignment_grade_type import EducationAssignmentGradeType
from .education_item_body import EducationItemBody
from .identity_set import IdentitySet
from .education_assignment_status import EducationAssignmentStatus
from .education_category import EducationCategory
from .education_grading_category import EducationGradingCategory
from .education_assignment_resource import EducationAssignmentResource
from .education_rubric import EducationRubric
from .education_submission import EducationSubmission

