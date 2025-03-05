from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class EducationSchool(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	externalSource: Optional[EducationExternalSource | str] = Field(alias="externalSource",default=None,)
	externalSourceDetail: Optional[str] = Field(alias="externalSourceDetail",default=None,)
	address: Optional[PhysicalAddress] = Field(alias="address",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	externalId: Optional[str] = Field(alias="externalId",default=None,)
	externalPrincipalId: Optional[str] = Field(alias="externalPrincipalId",default=None,)
	fax: Optional[str] = Field(alias="fax",default=None,)
	highestGrade: Optional[str] = Field(alias="highestGrade",default=None,)
	lowestGrade: Optional[str] = Field(alias="lowestGrade",default=None,)
	phone: Optional[str] = Field(alias="phone",default=None,)
	principalEmail: Optional[str] = Field(alias="principalEmail",default=None,)
	principalName: Optional[str] = Field(alias="principalName",default=None,)
	schoolNumber: Optional[str] = Field(alias="schoolNumber",default=None,)
	administrativeUnit: Optional[AdministrativeUnit] = Field(alias="administrativeUnit",default=None,)
	classes: Optional[list[EducationClass]] = Field(alias="classes",default=None,)
	users: Optional[list[EducationUser]] = Field(alias="users",default=None,)

from .education_external_source import EducationExternalSource
from .physical_address import PhysicalAddress
from .identity_set import IdentitySet
from .administrative_unit import AdministrativeUnit
from .education_class import EducationClass
from .education_user import EducationUser

