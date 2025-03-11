from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DomainDnsSrvRecordCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[DomainDnsSrvRecord]] = Field(alias="value",default=None,)

from .domain_dns_srv_record import DomainDnsSrvRecord

