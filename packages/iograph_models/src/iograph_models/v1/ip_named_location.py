from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class IpNamedLocation(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	modifiedDateTime: Optional[datetime] = Field(alias="modifiedDateTime", default=None,)
	ipRanges: Optional[list[Annotated[Union[IPv4CidrRange, IPv4Range, IPv6CidrRange, IPv6Range]],Field(discriminator="odata_type")]]] = Field(alias="ipRanges", default=None,)
	isTrusted: Optional[bool] = Field(alias="isTrusted", default=None,)

from .i_pv4_cidr_range import IPv4CidrRange
from .i_pv4_range import IPv4Range
from .i_pv6_cidr_range import IPv6CidrRange
from .i_pv6_range import IPv6Range

