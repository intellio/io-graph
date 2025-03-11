from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Contact(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	categories: Optional[list[str]] = Field(alias="categories",default=None,)
	changeKey: Optional[str] = Field(alias="changeKey",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	assistantName: Optional[str] = Field(alias="assistantName",default=None,)
	birthday: Optional[datetime] = Field(alias="birthday",default=None,)
	children: Optional[list[str]] = Field(alias="children",default=None,)
	companyName: Optional[str] = Field(alias="companyName",default=None,)
	department: Optional[str] = Field(alias="department",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	emailAddresses: Optional[list[TypedEmailAddress]] = Field(alias="emailAddresses",default=None,)
	fileAs: Optional[str] = Field(alias="fileAs",default=None,)
	flag: Optional[FollowupFlag] = Field(alias="flag",default=None,)
	gender: Optional[str] = Field(alias="gender",default=None,)
	generation: Optional[str] = Field(alias="generation",default=None,)
	givenName: Optional[str] = Field(alias="givenName",default=None,)
	imAddresses: Optional[list[str]] = Field(alias="imAddresses",default=None,)
	initials: Optional[str] = Field(alias="initials",default=None,)
	isFavorite: Optional[bool] = Field(alias="isFavorite",default=None,)
	jobTitle: Optional[str] = Field(alias="jobTitle",default=None,)
	manager: Optional[str] = Field(alias="manager",default=None,)
	middleName: Optional[str] = Field(alias="middleName",default=None,)
	nickName: Optional[str] = Field(alias="nickName",default=None,)
	officeLocation: Optional[str] = Field(alias="officeLocation",default=None,)
	parentFolderId: Optional[str] = Field(alias="parentFolderId",default=None,)
	personalNotes: Optional[str] = Field(alias="personalNotes",default=None,)
	phones: Optional[list[Phone]] = Field(alias="phones",default=None,)
	postalAddresses: Optional[list[PhysicalAddress]] = Field(alias="postalAddresses",default=None,)
	profession: Optional[str] = Field(alias="profession",default=None,)
	spouseName: Optional[str] = Field(alias="spouseName",default=None,)
	surname: Optional[str] = Field(alias="surname",default=None,)
	title: Optional[str] = Field(alias="title",default=None,)
	websites: Optional[list[Website]] = Field(alias="websites",default=None,)
	weddingAnniversary: Optional[str] = Field(alias="weddingAnniversary",default=None,)
	yomiCompanyName: Optional[str] = Field(alias="yomiCompanyName",default=None,)
	yomiGivenName: Optional[str] = Field(alias="yomiGivenName",default=None,)
	yomiSurname: Optional[str] = Field(alias="yomiSurname",default=None,)
	extensions: SerializeAsAny[Optional[list[Extension]]] = Field(alias="extensions",default=None,)
	multiValueExtendedProperties: Optional[list[MultiValueLegacyExtendedProperty]] = Field(alias="multiValueExtendedProperties",default=None,)
	photo: Optional[ProfilePhoto] = Field(alias="photo",default=None,)
	singleValueExtendedProperties: Optional[list[SingleValueLegacyExtendedProperty]] = Field(alias="singleValueExtendedProperties",default=None,)

from .typed_email_address import TypedEmailAddress
from .followup_flag import FollowupFlag
from .phone import Phone
from .physical_address import PhysicalAddress
from .website import Website
from .extension import Extension
from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
from .profile_photo import ProfilePhoto
from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty

