from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field


class AppleVpnConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[IosikEv2VpnConfiguration, MacOSVpnConfiguration],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .iosik_ev2_vpn_configuration import IosikEv2VpnConfiguration
from .mac_o_s_vpn_configuration import MacOSVpnConfiguration
