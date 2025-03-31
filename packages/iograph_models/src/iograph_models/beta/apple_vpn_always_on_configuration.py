from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AppleVpnAlwaysOnConfiguration(BaseModel):
	airPrintExceptionAction: Optional[VpnServiceExceptionAction | str] = Field(alias="airPrintExceptionAction", default=None,)
	allowAllCaptiveNetworkPlugins: Optional[bool] = Field(alias="allowAllCaptiveNetworkPlugins", default=None,)
	allowCaptiveWebSheet: Optional[bool] = Field(alias="allowCaptiveWebSheet", default=None,)
	allowedCaptiveNetworkPlugins: Optional[SpecifiedCaptiveNetworkPlugins] = Field(alias="allowedCaptiveNetworkPlugins", default=None,)
	cellularExceptionAction: Optional[VpnServiceExceptionAction | str] = Field(alias="cellularExceptionAction", default=None,)
	natKeepAliveIntervalInSeconds: Optional[int] = Field(alias="natKeepAliveIntervalInSeconds", default=None,)
	natKeepAliveOffloadEnable: Optional[bool] = Field(alias="natKeepAliveOffloadEnable", default=None,)
	tunnelConfiguration: Optional[VpnTunnelConfigurationType | str] = Field(alias="tunnelConfiguration", default=None,)
	userToggleEnabled: Optional[bool] = Field(alias="userToggleEnabled", default=None,)
	voicemailExceptionAction: Optional[VpnServiceExceptionAction | str] = Field(alias="voicemailExceptionAction", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .vpn_service_exception_action import VpnServiceExceptionAction
from .specified_captive_network_plugins import SpecifiedCaptiveNetworkPlugins
from .vpn_tunnel_configuration_type import VpnTunnelConfigurationType
