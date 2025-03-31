from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from pydantic import BaseModel, Field


class Person(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.person"] = Field(alias="@odata.type",)
	birthday: Optional[str] = Field(alias="birthday", default=None,)
	companyName: Optional[str] = Field(alias="companyName", default=None,)
	department: Optional[str] = Field(alias="department", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	givenName: Optional[str] = Field(alias="givenName", default=None,)
	imAddress: Optional[str] = Field(alias="imAddress", default=None,)
	isFavorite: Optional[bool] = Field(alias="isFavorite", default=None,)
	jobTitle: Optional[str] = Field(alias="jobTitle", default=None,)
	officeLocation: Optional[str] = Field(alias="officeLocation", default=None,)
	personNotes: Optional[str] = Field(alias="personNotes", default=None,)
	personType: Optional[PersonType] = Field(alias="personType", default=None,)
	phones: Optional[list[Phone]] = Field(alias="phones", default=None,)
	postalAddresses: Optional[list[Annotated[Union[LocationConstraintItem],Field(discriminator="odata_type")]]] = Field(alias="postalAddresses", default=None,)
	profession: Optional[str] = Field(alias="profession", default=None,)
	scoredEmailAddresses: Optional[list[ScoredEmailAddress]] = Field(alias="scoredEmailAddresses", default=None,)
	surname: Optional[str] = Field(alias="surname", default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName", default=None,)
	websites: Optional[list[Website]] = Field(alias="websites", default=None,)
	yomiCompany: Optional[str] = Field(alias="yomiCompany", default=None,)

from .person_type import PersonType
from .phone import Phone
from .location_constraint_item import LocationConstraintItem
from .scored_email_address import ScoredEmailAddress
from .website import Website
