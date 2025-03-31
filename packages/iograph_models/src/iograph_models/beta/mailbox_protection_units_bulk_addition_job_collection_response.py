from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MailboxProtectionUnitsBulkAdditionJobCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[MailboxProtectionUnitsBulkAdditionJob]] = Field(alias="value", default=None,)

from .mailbox_protection_units_bulk_addition_job import MailboxProtectionUnitsBulkAdditionJob
