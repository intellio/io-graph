from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsVpnConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[Windows10VpnConfiguration, Windows81VpnConfiguration, WindowsPhone81VpnConfiguration]],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .windows10_vpn_configuration import Windows10VpnConfiguration
from .windows81_vpn_configuration import Windows81VpnConfiguration
from .windows_phone81_vpn_configuration import WindowsPhone81VpnConfiguration

