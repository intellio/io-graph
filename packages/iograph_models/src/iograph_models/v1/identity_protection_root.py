from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class IdentityProtectionRoot(BaseModel):
	riskDetections: Optional[list[RiskDetection]] = Field(alias="riskDetections", default=None,)
	riskyServicePrincipals: Optional[list[Annotated[Union[RiskyServicePrincipalHistoryItem],Field(discriminator="odata_type")]]] = Field(alias="riskyServicePrincipals", default=None,)
	riskyUsers: Optional[list[Annotated[Union[RiskyUserHistoryItem],Field(discriminator="odata_type")]]] = Field(alias="riskyUsers", default=None,)
	servicePrincipalRiskDetections: Optional[list[ServicePrincipalRiskDetection]] = Field(alias="servicePrincipalRiskDetections", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .risk_detection import RiskDetection
from .risky_service_principal_history_item import RiskyServicePrincipalHistoryItem
from .risky_user_history_item import RiskyUserHistoryItem
from .service_principal_risk_detection import ServicePrincipalRiskDetection

