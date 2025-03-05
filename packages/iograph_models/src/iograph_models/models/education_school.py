from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class EducationSchool(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	externalSource: Optional[EducationExternalSource] = Field(default=None,alias="externalSource",)
	externalSourceDetail: Optional[str] = Field(default=None,alias="externalSourceDetail",)
	address: Optional[PhysicalAddress] = Field(default=None,alias="address",)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="createdBy",)
	externalId: Optional[str] = Field(default=None,alias="externalId",)
	externalPrincipalId: Optional[str] = Field(default=None,alias="externalPrincipalId",)
	fax: Optional[str] = Field(default=None,alias="fax",)
	highestGrade: Optional[str] = Field(default=None,alias="highestGrade",)
	lowestGrade: Optional[str] = Field(default=None,alias="lowestGrade",)
	phone: Optional[str] = Field(default=None,alias="phone",)
	principalEmail: Optional[str] = Field(default=None,alias="principalEmail",)
	principalName: Optional[str] = Field(default=None,alias="principalName",)
	schoolNumber: Optional[str] = Field(default=None,alias="schoolNumber",)
	administrativeUnit: Optional[AdministrativeUnit] = Field(default=None,alias="administrativeUnit",)
	classes: Optional[list[EducationClass]] = Field(default=None,alias="classes",)
	users: Optional[list[EducationUser]] = Field(default=None,alias="users",)

from .education_external_source import EducationExternalSource
from .physical_address import PhysicalAddress
from .identity_set import IdentitySet
from .administrative_unit import AdministrativeUnit
from .education_class import EducationClass
from .education_user import EducationUser

