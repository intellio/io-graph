from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DomainDnsMxRecordCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[DomainDnsMxRecord]] = Field(default=None,alias="value",)

from .domain_dns_mx_record import DomainDnsMxRecord

