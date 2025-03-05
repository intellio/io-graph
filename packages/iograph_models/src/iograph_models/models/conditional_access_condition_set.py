from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ConditionalAccessConditionSet(BaseModel):
	applications: Optional[ConditionalAccessApplications] = Field(alias="applications",default=None,)
	authenticationFlows: Optional[ConditionalAccessAuthenticationFlows] = Field(alias="authenticationFlows",default=None,)
	clientApplications: Optional[ConditionalAccessClientApplications] = Field(alias="clientApplications",default=None,)
	clientAppTypes: Optional[list[ConditionalAccessClientApp | str]] = Field(alias="clientAppTypes",default=None,)
	devices: Optional[ConditionalAccessDevices] = Field(alias="devices",default=None,)
	insiderRiskLevels: Optional[ConditionalAccessInsiderRiskLevels | str] = Field(alias="insiderRiskLevels",default=None,)
	locations: Optional[ConditionalAccessLocations] = Field(alias="locations",default=None,)
	platforms: Optional[ConditionalAccessPlatforms] = Field(alias="platforms",default=None,)
	servicePrincipalRiskLevels: Optional[list[RiskLevel | str]] = Field(alias="servicePrincipalRiskLevels",default=None,)
	signInRiskLevels: Optional[list[RiskLevel | str]] = Field(alias="signInRiskLevels",default=None,)
	userRiskLevels: Optional[list[RiskLevel | str]] = Field(alias="userRiskLevels",default=None,)
	users: Optional[ConditionalAccessUsers] = Field(alias="users",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .conditional_access_applications import ConditionalAccessApplications
from .conditional_access_authentication_flows import ConditionalAccessAuthenticationFlows
from .conditional_access_client_applications import ConditionalAccessClientApplications
from .conditional_access_client_app import ConditionalAccessClientApp
from .conditional_access_devices import ConditionalAccessDevices
from .conditional_access_insider_risk_levels import ConditionalAccessInsiderRiskLevels
from .conditional_access_locations import ConditionalAccessLocations
from .conditional_access_platforms import ConditionalAccessPlatforms
from .risk_level import RiskLevel
from .risk_level import RiskLevel
from .risk_level import RiskLevel
from .conditional_access_users import ConditionalAccessUsers

