from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class EducationUser(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	accountEnabled: Optional[bool] = Field(default=None,alias="accountEnabled",)
	assignedLicenses: Optional[list[AssignedLicense]] = Field(default=None,alias="assignedLicenses",)
	assignedPlans: Optional[list[AssignedPlan]] = Field(default=None,alias="assignedPlans",)
	businessPhones: Optional[list[str]] = Field(default=None,alias="businessPhones",)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="createdBy",)
	department: Optional[str] = Field(default=None,alias="department",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	externalSource: Optional[EducationExternalSource] = Field(default=None,alias="externalSource",)
	externalSourceDetail: Optional[str] = Field(default=None,alias="externalSourceDetail",)
	givenName: Optional[str] = Field(default=None,alias="givenName",)
	mail: Optional[str] = Field(default=None,alias="mail",)
	mailingAddress: Optional[PhysicalAddress] = Field(default=None,alias="mailingAddress",)
	mailNickname: Optional[str] = Field(default=None,alias="mailNickname",)
	middleName: Optional[str] = Field(default=None,alias="middleName",)
	mobilePhone: Optional[str] = Field(default=None,alias="mobilePhone",)
	officeLocation: Optional[str] = Field(default=None,alias="officeLocation",)
	onPremisesInfo: Optional[EducationOnPremisesInfo] = Field(default=None,alias="onPremisesInfo",)
	passwordPolicies: Optional[str] = Field(default=None,alias="passwordPolicies",)
	passwordProfile: Optional[PasswordProfile] = Field(default=None,alias="passwordProfile",)
	preferredLanguage: Optional[str] = Field(default=None,alias="preferredLanguage",)
	primaryRole: Optional[EducationUserRole] = Field(default=None,alias="primaryRole",)
	provisionedPlans: Optional[list[ProvisionedPlan]] = Field(default=None,alias="provisionedPlans",)
	refreshTokensValidFromDateTime: Optional[datetime] = Field(default=None,alias="refreshTokensValidFromDateTime",)
	relatedContacts: Optional[list[RelatedContact]] = Field(default=None,alias="relatedContacts",)
	residenceAddress: Optional[PhysicalAddress] = Field(default=None,alias="residenceAddress",)
	showInAddressList: Optional[bool] = Field(default=None,alias="showInAddressList",)
	student: Optional[EducationStudent] = Field(default=None,alias="student",)
	surname: Optional[str] = Field(default=None,alias="surname",)
	teacher: Optional[EducationTeacher] = Field(default=None,alias="teacher",)
	usageLocation: Optional[str] = Field(default=None,alias="usageLocation",)
	userPrincipalName: Optional[str] = Field(default=None,alias="userPrincipalName",)
	userType: Optional[str] = Field(default=None,alias="userType",)
	assignments: Optional[list[EducationAssignment]] = Field(default=None,alias="assignments",)
	classes: Optional[list[EducationClass]] = Field(default=None,alias="classes",)
	rubrics: Optional[list[EducationRubric]] = Field(default=None,alias="rubrics",)
	schools: Optional[list[EducationSchool]] = Field(default=None,alias="schools",)
	taughtClasses: Optional[list[EducationClass]] = Field(default=None,alias="taughtClasses",)
	user: Optional[User] = Field(default=None,alias="user",)

from .assigned_license import AssignedLicense
from .assigned_plan import AssignedPlan
from .identity_set import IdentitySet
from .education_external_source import EducationExternalSource
from .physical_address import PhysicalAddress
from .education_on_premises_info import EducationOnPremisesInfo
from .password_profile import PasswordProfile
from .education_user_role import EducationUserRole
from .provisioned_plan import ProvisionedPlan
from .related_contact import RelatedContact
from .physical_address import PhysicalAddress
from .education_student import EducationStudent
from .education_teacher import EducationTeacher
from .education_assignment import EducationAssignment
from .education_class import EducationClass
from .education_rubric import EducationRubric
from .education_school import EducationSchool
from .education_class import EducationClass
from .user import User

