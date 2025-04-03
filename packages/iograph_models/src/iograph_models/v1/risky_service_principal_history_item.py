from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class RiskyServicePrincipalHistoryItem(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.riskyServicePrincipalHistoryItem"] = Field(alias="@odata.type", default="#microsoft.graph.riskyServicePrincipalHistoryItem")
	appId: Optional[str] = Field(alias="appId", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	isEnabled: Optional[bool] = Field(alias="isEnabled", default=None,)
	isProcessing: Optional[bool] = Field(alias="isProcessing", default=None,)
	riskDetail: Optional[RiskDetail | str] = Field(alias="riskDetail", default=None,)
	riskLastUpdatedDateTime: Optional[datetime] = Field(alias="riskLastUpdatedDateTime", default=None,)
	riskLevel: Optional[RiskLevel | str] = Field(alias="riskLevel", default=None,)
	riskState: Optional[RiskState | str] = Field(alias="riskState", default=None,)
	servicePrincipalType: Optional[str] = Field(alias="servicePrincipalType", default=None,)
	history: Optional[list[RiskyServicePrincipalHistoryItem]] = Field(alias="history", default=None,)
	activity: Optional[RiskServicePrincipalActivity] = Field(alias="activity", default=None,)
	initiatedBy: Optional[str] = Field(alias="initiatedBy", default=None,)

from .risk_detail import RiskDetail
from .risk_level import RiskLevel
from .risk_state import RiskState
from .risk_service_principal_activity import RiskServicePrincipalActivity
