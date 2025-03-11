from __future__ import annotations
from uuid import UUID
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class GeneralLedgerEntry(BaseModel):
	accountId: Optional[UUID] = Field(alias="accountId",default=None,)
	accountNumber: Optional[str] = Field(alias="accountNumber",default=None,)
	creditAmount: Optional[int] = Field(alias="creditAmount",default=None,)
	debitAmount: Optional[int] = Field(alias="debitAmount",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	documentNumber: Optional[str] = Field(alias="documentNumber",default=None,)
	documentType: Optional[str] = Field(alias="documentType",default=None,)
	id: Optional[UUID] = Field(alias="id",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	postingDate: Optional[str] = Field(alias="postingDate",default=None,)
	account: Optional[Account] = Field(alias="account",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .account import Account

