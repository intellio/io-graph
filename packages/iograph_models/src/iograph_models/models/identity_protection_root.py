from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IdentityProtectionRoot(BaseModel):
	riskDetections: Optional[list[RiskDetection]] = Field(alias="riskDetections",default=None,)
	riskyServicePrincipals: SerializeAsAny[Optional[list[RiskyServicePrincipal]]] = Field(alias="riskyServicePrincipals",default=None,)
	riskyUsers: SerializeAsAny[Optional[list[RiskyUser]]] = Field(alias="riskyUsers",default=None,)
	servicePrincipalRiskDetections: Optional[list[ServicePrincipalRiskDetection]] = Field(alias="servicePrincipalRiskDetections",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .risk_detection import RiskDetection
from .risky_service_principal import RiskyServicePrincipal
from .risky_user import RiskyUser
from .service_principal_risk_detection import ServicePrincipalRiskDetection

