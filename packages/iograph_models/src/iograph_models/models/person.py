from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Person(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	birthday: Optional[str] = Field(default=None,alias="birthday",)
	companyName: Optional[str] = Field(default=None,alias="companyName",)
	department: Optional[str] = Field(default=None,alias="department",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	givenName: Optional[str] = Field(default=None,alias="givenName",)
	imAddress: Optional[str] = Field(default=None,alias="imAddress",)
	isFavorite: Optional[bool] = Field(default=None,alias="isFavorite",)
	jobTitle: Optional[str] = Field(default=None,alias="jobTitle",)
	officeLocation: Optional[str] = Field(default=None,alias="officeLocation",)
	personNotes: Optional[str] = Field(default=None,alias="personNotes",)
	personType: Optional[PersonType] = Field(default=None,alias="personType",)
	phones: list[Phone] = Field(alias="phones",)
	postalAddresses: list[Location] = Field(alias="postalAddresses",)
	profession: Optional[str] = Field(default=None,alias="profession",)
	scoredEmailAddresses: list[ScoredEmailAddress] = Field(alias="scoredEmailAddresses",)
	surname: Optional[str] = Field(default=None,alias="surname",)
	userPrincipalName: Optional[str] = Field(default=None,alias="userPrincipalName",)
	websites: list[Website] = Field(alias="websites",)
	yomiCompany: Optional[str] = Field(default=None,alias="yomiCompany",)

from .person_type import PersonType
from .phone import Phone
from .location import Location
from .scored_email_address import ScoredEmailAddress
from .website import Website

