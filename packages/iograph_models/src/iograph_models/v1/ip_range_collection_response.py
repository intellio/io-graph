from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class IpRangeCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[IPv4CidrRange, IPv4Range, IPv6CidrRange, IPv6Range]],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .i_pv4_cidr_range import IPv4CidrRange
from .i_pv4_range import IPv4Range
from .i_pv6_cidr_range import IPv6CidrRange
from .i_pv6_range import IPv6Range

