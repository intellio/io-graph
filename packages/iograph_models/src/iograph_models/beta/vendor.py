from __future__ import annotations
from uuid import UUID
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Vendor(BaseModel):
	address: Optional[PostalAddressType] = Field(alias="address", default=None,)
	balance: Optional[int] = Field(alias="balance", default=None,)
	blocked: Optional[str] = Field(alias="blocked", default=None,)
	currencyCode: Optional[str] = Field(alias="currencyCode", default=None,)
	currencyId: Optional[UUID] = Field(alias="currencyId", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	email: Optional[str] = Field(alias="email", default=None,)
	id: Optional[UUID] = Field(alias="id", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	number: Optional[str] = Field(alias="number", default=None,)
	paymentMethodId: Optional[UUID] = Field(alias="paymentMethodId", default=None,)
	paymentTermsId: Optional[UUID] = Field(alias="paymentTermsId", default=None,)
	phoneNumber: Optional[str] = Field(alias="phoneNumber", default=None,)
	taxLiable: Optional[bool] = Field(alias="taxLiable", default=None,)
	taxRegistrationNumber: Optional[str] = Field(alias="taxRegistrationNumber", default=None,)
	website: Optional[str] = Field(alias="website", default=None,)
	currency: Optional[Currency] = Field(alias="currency", default=None,)
	paymentMethod: Optional[PaymentMethod] = Field(alias="paymentMethod", default=None,)
	paymentTerm: Optional[PaymentTerm] = Field(alias="paymentTerm", default=None,)
	picture: Optional[list[Picture]] = Field(alias="picture", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .postal_address_type import PostalAddressType
from .currency import Currency
from .payment_method import PaymentMethod
from .payment_term import PaymentTerm
from .picture import Picture

