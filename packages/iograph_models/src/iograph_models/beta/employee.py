from __future__ import annotations
from uuid import UUID
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Employee(BaseModel):
	address: Optional[PostalAddressType] = Field(alias="address",default=None,)
	birthDate: Optional[str] = Field(alias="birthDate",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	email: Optional[str] = Field(alias="email",default=None,)
	employmentDate: Optional[str] = Field(alias="employmentDate",default=None,)
	givenName: Optional[str] = Field(alias="givenName",default=None,)
	id: Optional[UUID] = Field(alias="id",default=None,)
	jobTitle: Optional[str] = Field(alias="jobTitle",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	middleName: Optional[str] = Field(alias="middleName",default=None,)
	mobilePhone: Optional[str] = Field(alias="mobilePhone",default=None,)
	number: Optional[str] = Field(alias="number",default=None,)
	personalEmail: Optional[str] = Field(alias="personalEmail",default=None,)
	phoneNumber: Optional[str] = Field(alias="phoneNumber",default=None,)
	statisticsGroupCode: Optional[str] = Field(alias="statisticsGroupCode",default=None,)
	status: Optional[str] = Field(alias="status",default=None,)
	surname: Optional[str] = Field(alias="surname",default=None,)
	terminationDate: Optional[str] = Field(alias="terminationDate",default=None,)
	picture: Optional[list[Picture]] = Field(alias="picture",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .postal_address_type import PostalAddressType
from .picture import Picture

