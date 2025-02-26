from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class RiskyServicePrincipalHistoryItem(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	appId: Optional[str] = Field(default=None,alias="appId",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	isEnabled: Optional[bool] = Field(default=None,alias="isEnabled",)
	isProcessing: Optional[bool] = Field(default=None,alias="isProcessing",)
	riskDetail: Optional[RiskDetail] = Field(default=None,alias="riskDetail",)
	riskLastUpdatedDateTime: Optional[datetime] = Field(default=None,alias="riskLastUpdatedDateTime",)
	riskLevel: Optional[RiskLevel] = Field(default=None,alias="riskLevel",)
	riskState: Optional[RiskState] = Field(default=None,alias="riskState",)
	servicePrincipalType: Optional[str] = Field(default=None,alias="servicePrincipalType",)
	history: list[RiskyServicePrincipalHistoryItem] = Field(alias="history",)
	activity: Optional[RiskServicePrincipalActivity] = Field(default=None,alias="activity",)
	initiatedBy: Optional[str] = Field(default=None,alias="initiatedBy",)

from .risk_detail import RiskDetail
from .risk_level import RiskLevel
from .risk_state import RiskState
from .risk_service_principal_activity import RiskServicePrincipalActivity

