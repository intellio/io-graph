from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class RiskyUserHistoryItem(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	isDeleted: Optional[bool] = Field(default=None,alias="isDeleted",)
	isProcessing: Optional[bool] = Field(default=None,alias="isProcessing",)
	riskDetail: Optional[RiskDetail] = Field(default=None,alias="riskDetail",)
	riskLastUpdatedDateTime: Optional[datetime] = Field(default=None,alias="riskLastUpdatedDateTime",)
	riskLevel: Optional[RiskLevel] = Field(default=None,alias="riskLevel",)
	riskState: Optional[RiskState] = Field(default=None,alias="riskState",)
	userDisplayName: Optional[str] = Field(default=None,alias="userDisplayName",)
	userPrincipalName: Optional[str] = Field(default=None,alias="userPrincipalName",)
	history: Optional[list[RiskyUserHistoryItem]] = Field(default=None,alias="history",)
	activity: Optional[RiskUserActivity] = Field(default=None,alias="activity",)
	initiatedBy: Optional[str] = Field(default=None,alias="initiatedBy",)
	userId: Optional[str] = Field(default=None,alias="userId",)

from .risk_detail import RiskDetail
from .risk_level import RiskLevel
from .risk_state import RiskState
from .risk_user_activity import RiskUserActivity

