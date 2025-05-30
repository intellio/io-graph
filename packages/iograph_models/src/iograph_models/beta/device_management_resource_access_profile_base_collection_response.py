from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field


class DeviceManagementResourceAccessProfileBaseCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[Windows10XSCEPCertificateProfile, Windows10XTrustedRootCertificate, Windows10XVpnConfiguration, Windows10XWifiConfiguration],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .windows10_x_s_c_e_p_certificate_profile import Windows10XSCEPCertificateProfile
from .windows10_x_trusted_root_certificate import Windows10XTrustedRootCertificate
from .windows10_x_vpn_configuration import Windows10XVpnConfiguration
from .windows10_x_wifi_configuration import Windows10XWifiConfiguration
