from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityPassiveDnsRecordCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[SecurityPassiveDnsRecord]] = Field(alias="value", default=None,)

from .security_passive_dns_record import SecurityPassiveDnsRecord

