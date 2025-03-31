from __future__ import annotations
from uuid import UUID
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class JournalLine(BaseModel):
	accountId: Optional[UUID] = Field(alias="accountId", default=None,)
	accountNumber: Optional[str] = Field(alias="accountNumber", default=None,)
	amount: Optional[int] = Field(alias="amount", default=None,)
	comment: Optional[str] = Field(alias="comment", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	documentNumber: Optional[str] = Field(alias="documentNumber", default=None,)
	externalDocumentNumber: Optional[str] = Field(alias="externalDocumentNumber", default=None,)
	id: Optional[UUID] = Field(alias="id", default=None,)
	journalDisplayName: Optional[str] = Field(alias="journalDisplayName", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	lineNumber: Optional[int] = Field(alias="lineNumber", default=None,)
	postingDate: Optional[str] = Field(alias="postingDate", default=None,)
	account: Optional[Account] = Field(alias="account", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .account import Account
