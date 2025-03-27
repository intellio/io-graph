from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsInformationProtectionIPRangeCollection(BaseModel):
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	ranges: Optional[list[Annotated[Union[IPv4CidrRange, IPv4Range, IPv6CidrRange, IPv6Range],Field(discriminator="odata_type")]]] = Field(alias="ranges", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .i_pv4_cidr_range import IPv4CidrRange
from .i_pv4_range import IPv4Range
from .i_pv6_cidr_range import IPv6CidrRange
from .i_pv6_range import IPv6Range

