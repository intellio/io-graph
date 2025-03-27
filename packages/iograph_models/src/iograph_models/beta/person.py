from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class Person(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	birthday: Optional[str] = Field(alias="birthday", default=None,)
	companyName: Optional[str] = Field(alias="companyName", default=None,)
	department: Optional[str] = Field(alias="department", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	emailAddresses: Optional[list[RankedEmailAddress]] = Field(alias="emailAddresses", default=None,)
	givenName: Optional[str] = Field(alias="givenName", default=None,)
	isFavorite: Optional[bool] = Field(alias="isFavorite", default=None,)
	mailboxType: Optional[str] = Field(alias="mailboxType", default=None,)
	officeLocation: Optional[str] = Field(alias="officeLocation", default=None,)
	personNotes: Optional[str] = Field(alias="personNotes", default=None,)
	personType: Optional[str] = Field(alias="personType", default=None,)
	phones: Optional[list[Phone]] = Field(alias="phones", default=None,)
	postalAddresses: Optional[list[Annotated[Union[LocationConstraintItem],Field(discriminator="odata_type")]]] = Field(alias="postalAddresses", default=None,)
	profession: Optional[str] = Field(alias="profession", default=None,)
	sources: Optional[list[PersonDataSource]] = Field(alias="sources", default=None,)
	surname: Optional[str] = Field(alias="surname", default=None,)
	title: Optional[str] = Field(alias="title", default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName", default=None,)
	websites: Optional[list[Website]] = Field(alias="websites", default=None,)
	yomiCompany: Optional[str] = Field(alias="yomiCompany", default=None,)

from .ranked_email_address import RankedEmailAddress
from .phone import Phone
from .location_constraint_item import LocationConstraintItem
from .person_data_source import PersonDataSource
from .website import Website

