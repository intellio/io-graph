from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IdentityProtectionRoot(BaseModel):
	riskDetections: Optional[list[RiskDetection]] = Field(default=None,alias="riskDetections",)
	riskyServicePrincipals: SerializeAsAny[Optional[list[RiskyServicePrincipal]]] = Field(default=None,alias="riskyServicePrincipals",)
	riskyUsers: SerializeAsAny[Optional[list[RiskyUser]]] = Field(default=None,alias="riskyUsers",)
	servicePrincipalRiskDetections: Optional[list[ServicePrincipalRiskDetection]] = Field(default=None,alias="servicePrincipalRiskDetections",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .risk_detection import RiskDetection
from .risky_service_principal import RiskyServicePrincipal
from .risky_user import RiskyUser
from .service_principal_risk_detection import ServicePrincipalRiskDetection

