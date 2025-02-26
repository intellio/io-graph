from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ConditionalAccessConditionSet(BaseModel):
	applications: Optional[ConditionalAccessApplications] = Field(default=None,alias="applications",)
	authenticationFlows: Optional[ConditionalAccessAuthenticationFlows] = Field(default=None,alias="authenticationFlows",)
	clientApplications: Optional[ConditionalAccessClientApplications] = Field(default=None,alias="clientApplications",)
	clientAppTypes: list[ConditionalAccessClientApp] = Field(alias="clientAppTypes",)
	devices: Optional[ConditionalAccessDevices] = Field(default=None,alias="devices",)
	insiderRiskLevels: Optional[ConditionalAccessInsiderRiskLevels] = Field(default=None,alias="insiderRiskLevels",)
	locations: Optional[ConditionalAccessLocations] = Field(default=None,alias="locations",)
	platforms: Optional[ConditionalAccessPlatforms] = Field(default=None,alias="platforms",)
	servicePrincipalRiskLevels: list[RiskLevel] = Field(alias="servicePrincipalRiskLevels",)
	signInRiskLevels: list[RiskLevel] = Field(alias="signInRiskLevels",)
	userRiskLevels: list[RiskLevel] = Field(alias="userRiskLevels",)
	users: Optional[ConditionalAccessUsers] = Field(default=None,alias="users",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

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

