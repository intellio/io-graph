from __future__ import annotations
from uuid import UUID
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class CustomerPaymentJournal(BaseModel):
	balancingAccountId: Optional[UUID] = Field(alias="balancingAccountId", default=None,)
	balancingAccountNumber: Optional[str] = Field(alias="balancingAccountNumber", default=None,)
	code: Optional[str] = Field(alias="code", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	id: Optional[UUID] = Field(alias="id", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	account: Optional[Account] = Field(alias="account", default=None,)
	customerPayments: Optional[list[CustomerPayment]] = Field(alias="customerPayments", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .account import Account
from .customer_payment import CustomerPayment
