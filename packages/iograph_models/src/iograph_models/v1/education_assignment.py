from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class EducationAssignment(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.educationAssignment"] = Field(alias="@odata.type", default="#microsoft.graph.educationAssignment")
	addedStudentAction: Optional[EducationAddedStudentAction | str] = Field(alias="addedStudentAction", default=None,)
	addToCalendarAction: Optional[EducationAddToCalendarOptions | str] = Field(alias="addToCalendarAction", default=None,)
	allowLateSubmissions: Optional[bool] = Field(alias="allowLateSubmissions", default=None,)
	allowStudentsToAddResourcesToSubmission: Optional[bool] = Field(alias="allowStudentsToAddResourcesToSubmission", default=None,)
	assignDateTime: Optional[datetime] = Field(alias="assignDateTime", default=None,)
	assignedDateTime: Optional[datetime] = Field(alias="assignedDateTime", default=None,)
	assignTo: Optional[Union[EducationAssignmentClassRecipient, EducationAssignmentGroupRecipient, EducationAssignmentIndividualRecipient]] = Field(alias="assignTo", default=None,discriminator="odata_type", )
	classId: Optional[str] = Field(alias="classId", default=None,)
	closeDateTime: Optional[datetime] = Field(alias="closeDateTime", default=None,)
	createdBy: Optional[Union[ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="createdBy", default=None,discriminator="odata_type", )
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	dueDateTime: Optional[datetime] = Field(alias="dueDateTime", default=None,)
	feedbackResourcesFolderUrl: Optional[str] = Field(alias="feedbackResourcesFolderUrl", default=None,)
	grading: Optional[Union[EducationAssignmentPointsGradeType]] = Field(alias="grading", default=None,discriminator="odata_type", )
	instructions: Optional[EducationItemBody] = Field(alias="instructions", default=None,)
	lastModifiedBy: Optional[Union[ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="lastModifiedBy", default=None,discriminator="odata_type", )
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	moduleUrl: Optional[str] = Field(alias="moduleUrl", default=None,)
	notificationChannelUrl: Optional[str] = Field(alias="notificationChannelUrl", default=None,)
	resourcesFolderUrl: Optional[str] = Field(alias="resourcesFolderUrl", default=None,)
	status: Optional[EducationAssignmentStatus | str] = Field(alias="status", default=None,)
	webUrl: Optional[str] = Field(alias="webUrl", default=None,)
	categories: Optional[list[EducationCategory]] = Field(alias="categories", default=None,)
	gradingCategory: Optional[EducationGradingCategory] = Field(alias="gradingCategory", default=None,)
	resources: Optional[list[EducationAssignmentResource]] = Field(alias="resources", default=None,)
	rubric: Optional[EducationRubric] = Field(alias="rubric", default=None,)
	submissions: Optional[list[EducationSubmission]] = Field(alias="submissions", default=None,)

from .education_added_student_action import EducationAddedStudentAction
from .education_add_to_calendar_options import EducationAddToCalendarOptions
from .education_assignment_class_recipient import EducationAssignmentClassRecipient
from .education_assignment_group_recipient import EducationAssignmentGroupRecipient
from .education_assignment_individual_recipient import EducationAssignmentIndividualRecipient
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .education_assignment_points_grade_type import EducationAssignmentPointsGradeType
from .education_item_body import EducationItemBody
from .education_assignment_status import EducationAssignmentStatus
from .education_category import EducationCategory
from .education_grading_category import EducationGradingCategory
from .education_assignment_resource import EducationAssignmentResource
from .education_rubric import EducationRubric
from .education_submission import EducationSubmission
