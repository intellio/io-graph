from __future__ import annotations
from uuid import UUID
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class CompanyInformation(BaseModel):
	address: Optional[PostalAddressType] = Field(alias="address",default=None,)
	currencyCode: Optional[str] = Field(alias="currencyCode",default=None,)
	currentFiscalYearStartDate: Optional[str] = Field(alias="currentFiscalYearStartDate",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	email: Optional[str] = Field(alias="email",default=None,)
	faxNumber: Optional[str] = Field(alias="faxNumber",default=None,)
	id: Optional[UUID] = Field(alias="id",default=None,)
	industry: Optional[str] = Field(alias="industry",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	phoneNumber: Optional[str] = Field(alias="phoneNumber",default=None,)
	picture: Optional[str] = Field(alias="picture",default=None,)
	taxRegistrationNumber: Optional[str] = Field(alias="taxRegistrationNumber",default=None,)
	website: Optional[str] = Field(alias="website",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .postal_address_type import PostalAddressType

