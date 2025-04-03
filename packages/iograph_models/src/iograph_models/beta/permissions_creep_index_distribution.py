from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class PermissionsCreepIndexDistribution(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.permissionsCreepIndexDistribution"] = Field(alias="@odata.type", default="#microsoft.graph.permissionsCreepIndexDistribution")
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	highRiskProfile: Optional[RiskProfile] = Field(alias="highRiskProfile", default=None,)
	lowRiskProfile: Optional[RiskProfile] = Field(alias="lowRiskProfile", default=None,)
	mediumRiskProfile: Optional[RiskProfile] = Field(alias="mediumRiskProfile", default=None,)
	authorizationSystem: Optional[Union[AwsAuthorizationSystem, AzureAuthorizationSystem, GcpAuthorizationSystem]] = Field(alias="authorizationSystem", default=None,discriminator="odata_type", )

from .risk_profile import RiskProfile
from .aws_authorization_system import AwsAuthorizationSystem
from .azure_authorization_system import AzureAuthorizationSystem
from .gcp_authorization_system import GcpAuthorizationSystem
