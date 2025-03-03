from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class EducationClass(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	classCode: Optional[str] = Field(default=None,alias="classCode",)
	course: Optional[EducationCourse] = Field(default=None,alias="course",)
	createdBy: Optional[IdentitySet] = Field(default=None,alias="createdBy",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	externalId: Optional[str] = Field(default=None,alias="externalId",)
	externalName: Optional[str] = Field(default=None,alias="externalName",)
	externalSource: Optional[EducationExternalSource] = Field(default=None,alias="externalSource",)
	externalSourceDetail: Optional[str] = Field(default=None,alias="externalSourceDetail",)
	grade: Optional[str] = Field(default=None,alias="grade",)
	mailNickname: Optional[str] = Field(default=None,alias="mailNickname",)
	term: Optional[EducationTerm] = Field(default=None,alias="term",)
	assignmentCategories: Optional[list[EducationCategory]] = Field(default=None,alias="assignmentCategories",)
	assignmentDefaults: Optional[EducationAssignmentDefaults] = Field(default=None,alias="assignmentDefaults",)
	assignments: Optional[list[EducationAssignment]] = Field(default=None,alias="assignments",)
	assignmentSettings: Optional[EducationAssignmentSettings] = Field(default=None,alias="assignmentSettings",)
	group: Optional[Group] = Field(default=None,alias="group",)
	members: Optional[list[EducationUser]] = Field(default=None,alias="members",)
	modules: Optional[list[EducationModule]] = Field(default=None,alias="modules",)
	schools: Optional[list[EducationSchool]] = Field(default=None,alias="schools",)
	teachers: Optional[list[EducationUser]] = Field(default=None,alias="teachers",)

from .education_course import EducationCourse
from .identity_set import IdentitySet
from .education_external_source import EducationExternalSource
from .education_term import EducationTerm
from .education_category import EducationCategory
from .education_assignment_defaults import EducationAssignmentDefaults
from .education_assignment import EducationAssignment
from .education_assignment_settings import EducationAssignmentSettings
from .group import Group
from .education_user import EducationUser
from .education_module import EducationModule
from .education_school import EducationSchool
from .education_user import EducationUser

