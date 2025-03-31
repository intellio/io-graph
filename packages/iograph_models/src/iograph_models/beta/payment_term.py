from __future__ import annotations
from uuid import UUID
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class PaymentTerm(BaseModel):
	calculateDiscountOnCreditMemos: Optional[bool] = Field(alias="calculateDiscountOnCreditMemos", default=None,)
	code: Optional[str] = Field(alias="code", default=None,)
	discountDateCalculation: Optional[str] = Field(alias="discountDateCalculation", default=None,)
	discountPercent: Optional[int] = Field(alias="discountPercent", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	dueDateCalculation: Optional[str] = Field(alias="dueDateCalculation", default=None,)
	id: Optional[UUID] = Field(alias="id", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

