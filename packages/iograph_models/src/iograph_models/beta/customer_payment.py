from __future__ import annotations
from uuid import UUID
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class CustomerPayment(BaseModel):
	amount: Optional[int] = Field(alias="amount", default=None,)
	appliesToInvoiceId: Optional[UUID] = Field(alias="appliesToInvoiceId", default=None,)
	appliesToInvoiceNumber: Optional[str] = Field(alias="appliesToInvoiceNumber", default=None,)
	comment: Optional[str] = Field(alias="comment", default=None,)
	contactId: Optional[str] = Field(alias="contactId", default=None,)
	customerId: Optional[UUID] = Field(alias="customerId", default=None,)
	customerNumber: Optional[str] = Field(alias="customerNumber", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	documentNumber: Optional[str] = Field(alias="documentNumber", default=None,)
	externalDocumentNumber: Optional[str] = Field(alias="externalDocumentNumber", default=None,)
	id: Optional[UUID] = Field(alias="id", default=None,)
	journalDisplayName: Optional[str] = Field(alias="journalDisplayName", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	lineNumber: Optional[int] = Field(alias="lineNumber", default=None,)
	postingDate: Optional[str] = Field(alias="postingDate", default=None,)
	customer: Optional[Customer] = Field(alias="customer", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .customer import Customer

