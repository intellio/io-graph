from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityWhoisRecordCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[SecurityWhoisRecord]] = Field(alias="value", default=None,)

from .security_whois_record import SecurityWhoisRecord
