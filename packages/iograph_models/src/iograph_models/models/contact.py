from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Contact(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	categories: Optional[list[str]] = Field(default=None,alias="categories",)
	changeKey: Optional[str] = Field(default=None,alias="changeKey",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	assistantName: Optional[str] = Field(default=None,alias="assistantName",)
	birthday: Optional[datetime] = Field(default=None,alias="birthday",)
	businessAddress: Optional[PhysicalAddress] = Field(default=None,alias="businessAddress",)
	businessHomePage: Optional[str] = Field(default=None,alias="businessHomePage",)
	businessPhones: Optional[list[str]] = Field(default=None,alias="businessPhones",)
	children: Optional[list[str]] = Field(default=None,alias="children",)
	companyName: Optional[str] = Field(default=None,alias="companyName",)
	department: Optional[str] = Field(default=None,alias="department",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	emailAddresses: Optional[list[EmailAddress]] = Field(default=None,alias="emailAddresses",)
	fileAs: Optional[str] = Field(default=None,alias="fileAs",)
	generation: Optional[str] = Field(default=None,alias="generation",)
	givenName: Optional[str] = Field(default=None,alias="givenName",)
	homeAddress: Optional[PhysicalAddress] = Field(default=None,alias="homeAddress",)
	homePhones: Optional[list[str]] = Field(default=None,alias="homePhones",)
	imAddresses: Optional[list[str]] = Field(default=None,alias="imAddresses",)
	initials: Optional[str] = Field(default=None,alias="initials",)
	jobTitle: Optional[str] = Field(default=None,alias="jobTitle",)
	manager: Optional[str] = Field(default=None,alias="manager",)
	middleName: Optional[str] = Field(default=None,alias="middleName",)
	mobilePhone: Optional[str] = Field(default=None,alias="mobilePhone",)
	nickName: Optional[str] = Field(default=None,alias="nickName",)
	officeLocation: Optional[str] = Field(default=None,alias="officeLocation",)
	otherAddress: Optional[PhysicalAddress] = Field(default=None,alias="otherAddress",)
	parentFolderId: Optional[str] = Field(default=None,alias="parentFolderId",)
	personalNotes: Optional[str] = Field(default=None,alias="personalNotes",)
	profession: Optional[str] = Field(default=None,alias="profession",)
	spouseName: Optional[str] = Field(default=None,alias="spouseName",)
	surname: Optional[str] = Field(default=None,alias="surname",)
	title: Optional[str] = Field(default=None,alias="title",)
	yomiCompanyName: Optional[str] = Field(default=None,alias="yomiCompanyName",)
	yomiGivenName: Optional[str] = Field(default=None,alias="yomiGivenName",)
	yomiSurname: Optional[str] = Field(default=None,alias="yomiSurname",)
	extensions: SerializeAsAny[Optional[list[Extension]]] = Field(default=None,alias="extensions",)
	multiValueExtendedProperties: Optional[list[MultiValueLegacyExtendedProperty]] = Field(default=None,alias="multiValueExtendedProperties",)
	photo: Optional[ProfilePhoto] = Field(default=None,alias="photo",)
	singleValueExtendedProperties: Optional[list[SingleValueLegacyExtendedProperty]] = Field(default=None,alias="singleValueExtendedProperties",)

from .physical_address import PhysicalAddress
from .email_address import EmailAddress
from .physical_address import PhysicalAddress
from .physical_address import PhysicalAddress
from .extension import Extension
from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
from .profile_photo import ProfilePhoto
from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty

