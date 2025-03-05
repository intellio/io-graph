from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class EducationAssignment(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	addedStudentAction: Optional[str | EducationAddedStudentAction] = Field(alias="addedStudentAction",default=None,)
	addToCalendarAction: Optional[str | EducationAddToCalendarOptions] = Field(alias="addToCalendarAction",default=None,)
	allowLateSubmissions: Optional[bool] = Field(alias="allowLateSubmissions",default=None,)
	allowStudentsToAddResourcesToSubmission: Optional[bool] = Field(alias="allowStudentsToAddResourcesToSubmission",default=None,)
	assignDateTime: Optional[datetime] = Field(alias="assignDateTime",default=None,)
	assignedDateTime: Optional[datetime] = Field(alias="assignedDateTime",default=None,)
	assignTo: SerializeAsAny[Optional[EducationAssignmentRecipient]] = Field(alias="assignTo",default=None,)
	classId: Optional[str] = Field(alias="classId",default=None,)
	closeDateTime: Optional[datetime] = Field(alias="closeDateTime",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	dueDateTime: Optional[datetime] = Field(alias="dueDateTime",default=None,)
	feedbackResourcesFolderUrl: Optional[str] = Field(alias="feedbackResourcesFolderUrl",default=None,)
	grading: SerializeAsAny[Optional[EducationAssignmentGradeType]] = Field(alias="grading",default=None,)
	instructions: Optional[EducationItemBody] = Field(alias="instructions",default=None,)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	moduleUrl: Optional[str] = Field(alias="moduleUrl",default=None,)
	notificationChannelUrl: Optional[str] = Field(alias="notificationChannelUrl",default=None,)
	resourcesFolderUrl: Optional[str] = Field(alias="resourcesFolderUrl",default=None,)
	status: Optional[str | EducationAssignmentStatus] = Field(alias="status",default=None,)
	webUrl: Optional[str] = Field(alias="webUrl",default=None,)
	categories: Optional[list[EducationCategory]] = Field(alias="categories",default=None,)
	gradingCategory: Optional[EducationGradingCategory] = Field(alias="gradingCategory",default=None,)
	resources: Optional[list[EducationAssignmentResource]] = Field(alias="resources",default=None,)
	rubric: Optional[EducationRubric] = Field(alias="rubric",default=None,)
	submissions: Optional[list[EducationSubmission]] = Field(alias="submissions",default=None,)

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

