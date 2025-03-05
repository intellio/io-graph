from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MailboxProtectionUnitCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[MailboxProtectionUnit]] = Field(default=None,alias="value",)

from .mailbox_protection_unit import MailboxProtectionUnit

