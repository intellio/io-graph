from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IdentityProtectionRoot(BaseModel):
	riskDetections: list[RiskDetection] = Field(alias="riskDetections",)
	riskyServicePrincipals: list[RiskyServicePrincipal] = Field(alias="riskyServicePrincipals",)
	riskyUsers: list[RiskyUser] = Field(alias="riskyUsers",)
	servicePrincipalRiskDetections: list[ServicePrincipalRiskDetection] = Field(alias="servicePrincipalRiskDetections",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .risk_detection import RiskDetection
from .risky_service_principal import RiskyServicePrincipal
from .risky_user import RiskyUser
from .service_principal_risk_detection import ServicePrincipalRiskDetection

