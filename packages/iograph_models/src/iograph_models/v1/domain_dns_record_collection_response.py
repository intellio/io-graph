from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class DomainDnsRecordCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[DomainDnsCnameRecord, DomainDnsMxRecord, DomainDnsSrvRecord, DomainDnsTxtRecord, DomainDnsUnavailableRecord]],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .domain_dns_cname_record import DomainDnsCnameRecord
from .domain_dns_mx_record import DomainDnsMxRecord
from .domain_dns_srv_record import DomainDnsSrvRecord
from .domain_dns_txt_record import DomainDnsTxtRecord
from .domain_dns_unavailable_record import DomainDnsUnavailableRecord

