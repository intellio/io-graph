from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class EducationClass(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	classCode: Optional[str] = Field(alias="classCode",default=None,)
	course: Optional[EducationCourse] = Field(alias="course",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	externalId: Optional[str] = Field(alias="externalId",default=None,)
	externalName: Optional[str] = Field(alias="externalName",default=None,)
	externalSource: Optional[EducationExternalSource | str] = Field(alias="externalSource",default=None,)
	externalSourceDetail: Optional[str] = Field(alias="externalSourceDetail",default=None,)
	grade: Optional[str] = Field(alias="grade",default=None,)
	mailNickname: Optional[str] = Field(alias="mailNickname",default=None,)
	term: Optional[EducationTerm] = Field(alias="term",default=None,)
	assignmentCategories: Optional[list[EducationCategory]] = Field(alias="assignmentCategories",default=None,)
	assignmentDefaults: Optional[EducationAssignmentDefaults] = Field(alias="assignmentDefaults",default=None,)
	assignments: Optional[list[EducationAssignment]] = Field(alias="assignments",default=None,)
	assignmentSettings: Optional[EducationAssignmentSettings] = Field(alias="assignmentSettings",default=None,)
	group: Optional[Group] = Field(alias="group",default=None,)
	members: Optional[list[EducationUser]] = Field(alias="members",default=None,)
	modules: Optional[list[EducationModule]] = Field(alias="modules",default=None,)
	schools: Optional[list[EducationSchool]] = Field(alias="schools",default=None,)
	teachers: Optional[list[EducationUser]] = Field(alias="teachers",default=None,)

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

