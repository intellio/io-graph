from __future__ import annotations
from uuid import UUID
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AgedAccountsReceivable(BaseModel):
	agedAsOfDate: Optional[str] = Field(alias="agedAsOfDate",default=None,)
	balanceDue: Optional[int] = Field(alias="balanceDue",default=None,)
	currencyCode: Optional[str] = Field(alias="currencyCode",default=None,)
	currentAmount: Optional[int] = Field(alias="currentAmount",default=None,)
	customerId: Optional[str] = Field(alias="customerId",default=None,)
	customerNumber: Optional[str] = Field(alias="customerNumber",default=None,)
	id: Optional[UUID] = Field(alias="id",default=None,)
	name: Optional[str] = Field(alias="name",default=None,)
	period1Amount: Optional[int] = Field(alias="period1Amount",default=None,)
	period2Amount: Optional[int] = Field(alias="period2Amount",default=None,)
	period3Amount: Optional[int] = Field(alias="period3Amount",default=None,)
	periodLengthFilter: Optional[str] = Field(alias="periodLengthFilter",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


