from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Contact(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.contact"] = Field(alias="@odata.type", default="#microsoft.graph.contact")
	categories: Optional[list[str]] = Field(alias="categories", default=None,)
	changeKey: Optional[str] = Field(alias="changeKey", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	assistantName: Optional[str] = Field(alias="assistantName", default=None,)
	birthday: Optional[datetime] = Field(alias="birthday", default=None,)
	businessAddress: Optional[PhysicalAddress] = Field(alias="businessAddress", default=None,)
	businessHomePage: Optional[str] = Field(alias="businessHomePage", default=None,)
	businessPhones: Optional[list[str]] = Field(alias="businessPhones", default=None,)
	children: Optional[list[str]] = Field(alias="children", default=None,)
	companyName: Optional[str] = Field(alias="companyName", default=None,)
	department: Optional[str] = Field(alias="department", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	emailAddresses: Optional[list[EmailAddress]] = Field(alias="emailAddresses", default=None,)
	fileAs: Optional[str] = Field(alias="fileAs", default=None,)
	generation: Optional[str] = Field(alias="generation", default=None,)
	givenName: Optional[str] = Field(alias="givenName", default=None,)
	homeAddress: Optional[PhysicalAddress] = Field(alias="homeAddress", default=None,)
	homePhones: Optional[list[str]] = Field(alias="homePhones", default=None,)
	imAddresses: Optional[list[str]] = Field(alias="imAddresses", default=None,)
	initials: Optional[str] = Field(alias="initials", default=None,)
	jobTitle: Optional[str] = Field(alias="jobTitle", default=None,)
	manager: Optional[str] = Field(alias="manager", default=None,)
	middleName: Optional[str] = Field(alias="middleName", default=None,)
	mobilePhone: Optional[str] = Field(alias="mobilePhone", default=None,)
	nickName: Optional[str] = Field(alias="nickName", default=None,)
	officeLocation: Optional[str] = Field(alias="officeLocation", default=None,)
	otherAddress: Optional[PhysicalAddress] = Field(alias="otherAddress", default=None,)
	parentFolderId: Optional[str] = Field(alias="parentFolderId", default=None,)
	personalNotes: Optional[str] = Field(alias="personalNotes", default=None,)
	profession: Optional[str] = Field(alias="profession", default=None,)
	spouseName: Optional[str] = Field(alias="spouseName", default=None,)
	surname: Optional[str] = Field(alias="surname", default=None,)
	title: Optional[str] = Field(alias="title", default=None,)
	yomiCompanyName: Optional[str] = Field(alias="yomiCompanyName", default=None,)
	yomiGivenName: Optional[str] = Field(alias="yomiGivenName", default=None,)
	yomiSurname: Optional[str] = Field(alias="yomiSurname", default=None,)
	extensions: Optional[list[Annotated[Union[OpenTypeExtension],Field(discriminator="odata_type")]]] = Field(alias="extensions", default=None,)
	multiValueExtendedProperties: Optional[list[MultiValueLegacyExtendedProperty]] = Field(alias="multiValueExtendedProperties", default=None,)
	photo: Optional[ProfilePhoto] = Field(alias="photo", default=None,)
	singleValueExtendedProperties: Optional[list[SingleValueLegacyExtendedProperty]] = Field(alias="singleValueExtendedProperties", default=None,)

from .physical_address import PhysicalAddress
from .email_address import EmailAddress
from .physical_address import PhysicalAddress
from .physical_address import PhysicalAddress
from .open_type_extension import OpenTypeExtension
from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
from .profile_photo import ProfilePhoto
from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty

