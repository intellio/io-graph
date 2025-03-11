from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class PermissionsCreepIndexDistribution(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	highRiskProfile: Optional[RiskProfile] = Field(alias="highRiskProfile",default=None,)
	lowRiskProfile: Optional[RiskProfile] = Field(alias="lowRiskProfile",default=None,)
	mediumRiskProfile: Optional[RiskProfile] = Field(alias="mediumRiskProfile",default=None,)
	authorizationSystem: SerializeAsAny[Optional[AuthorizationSystem]] = Field(alias="authorizationSystem",default=None,)

from .risk_profile import RiskProfile
from .risk_profile import RiskProfile
from .risk_profile import RiskProfile
from .authorization_system import AuthorizationSystem

