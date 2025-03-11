from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ConditionalAccessWhatIfConditions(BaseModel):
	authenticationFlow: Optional[AuthenticationFlow] = Field(alias="authenticationFlow",default=None,)
	clientAppType: Optional[ConditionalAccessClientApp | str] = Field(alias="clientAppType",default=None,)
	country: Optional[str] = Field(alias="country",default=None,)
	deviceInfo: Optional[DeviceInfo] = Field(alias="deviceInfo",default=None,)
	devicePlatform: Optional[ConditionalAccessDevicePlatform | str] = Field(alias="devicePlatform",default=None,)
	insiderRiskLevel: Optional[InsiderRiskLevel | str] = Field(alias="insiderRiskLevel",default=None,)
	ipAddress: Optional[str] = Field(alias="ipAddress",default=None,)
	servicePrincipalRiskLevel: Optional[RiskLevel | str] = Field(alias="servicePrincipalRiskLevel",default=None,)
	signInRiskLevel: Optional[RiskLevel | str] = Field(alias="signInRiskLevel",default=None,)
	userRiskLevel: Optional[RiskLevel | str] = Field(alias="userRiskLevel",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .authentication_flow import AuthenticationFlow
from .conditional_access_client_app import ConditionalAccessClientApp
from .device_info import DeviceInfo
from .conditional_access_device_platform import ConditionalAccessDevicePlatform
from .insider_risk_level import InsiderRiskLevel
from .risk_level import RiskLevel
from .risk_level import RiskLevel
from .risk_level import RiskLevel

