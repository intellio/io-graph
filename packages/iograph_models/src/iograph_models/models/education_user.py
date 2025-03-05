from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class EducationUser(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	accountEnabled: Optional[bool] = Field(alias="accountEnabled",default=None,)
	assignedLicenses: Optional[list[AssignedLicense]] = Field(alias="assignedLicenses",default=None,)
	assignedPlans: Optional[list[AssignedPlan]] = Field(alias="assignedPlans",default=None,)
	businessPhones: Optional[list[str]] = Field(alias="businessPhones",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	department: Optional[str] = Field(alias="department",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	externalSource: Optional[str | EducationExternalSource] = Field(alias="externalSource",default=None,)
	externalSourceDetail: Optional[str] = Field(alias="externalSourceDetail",default=None,)
	givenName: Optional[str] = Field(alias="givenName",default=None,)
	mail: Optional[str] = Field(alias="mail",default=None,)
	mailingAddress: Optional[PhysicalAddress] = Field(alias="mailingAddress",default=None,)
	mailNickname: Optional[str] = Field(alias="mailNickname",default=None,)
	middleName: Optional[str] = Field(alias="middleName",default=None,)
	mobilePhone: Optional[str] = Field(alias="mobilePhone",default=None,)
	officeLocation: Optional[str] = Field(alias="officeLocation",default=None,)
	onPremisesInfo: Optional[EducationOnPremisesInfo] = Field(alias="onPremisesInfo",default=None,)
	passwordPolicies: Optional[str] = Field(alias="passwordPolicies",default=None,)
	passwordProfile: Optional[PasswordProfile] = Field(alias="passwordProfile",default=None,)
	preferredLanguage: Optional[str] = Field(alias="preferredLanguage",default=None,)
	primaryRole: Optional[str | EducationUserRole] = Field(alias="primaryRole",default=None,)
	provisionedPlans: Optional[list[ProvisionedPlan]] = Field(alias="provisionedPlans",default=None,)
	refreshTokensValidFromDateTime: Optional[datetime] = Field(alias="refreshTokensValidFromDateTime",default=None,)
	relatedContacts: Optional[list[RelatedContact]] = Field(alias="relatedContacts",default=None,)
	residenceAddress: Optional[PhysicalAddress] = Field(alias="residenceAddress",default=None,)
	showInAddressList: Optional[bool] = Field(alias="showInAddressList",default=None,)
	student: Optional[EducationStudent] = Field(alias="student",default=None,)
	surname: Optional[str] = Field(alias="surname",default=None,)
	teacher: Optional[EducationTeacher] = Field(alias="teacher",default=None,)
	usageLocation: Optional[str] = Field(alias="usageLocation",default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName",default=None,)
	userType: Optional[str] = Field(alias="userType",default=None,)
	assignments: Optional[list[EducationAssignment]] = Field(alias="assignments",default=None,)
	classes: Optional[list[EducationClass]] = Field(alias="classes",default=None,)
	rubrics: Optional[list[EducationRubric]] = Field(alias="rubrics",default=None,)
	schools: Optional[list[EducationSchool]] = Field(alias="schools",default=None,)
	taughtClasses: Optional[list[EducationClass]] = Field(alias="taughtClasses",default=None,)
	user: Optional[User] = Field(alias="user",default=None,)

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

