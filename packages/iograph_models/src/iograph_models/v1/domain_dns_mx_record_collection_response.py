from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DomainDnsMxRecordCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[DomainDnsMxRecord]] = Field(alias="value", default=None,)

from .domain_dns_mx_record import DomainDnsMxRecord
