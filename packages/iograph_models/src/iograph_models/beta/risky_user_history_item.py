from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class RiskyUserHistoryItem(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	isDeleted: Optional[bool] = Field(alias="isDeleted", default=None,)
	isProcessing: Optional[bool] = Field(alias="isProcessing", default=None,)
	riskDetail: Optional[RiskDetail | str] = Field(alias="riskDetail", default=None,)
	riskLastUpdatedDateTime: Optional[datetime] = Field(alias="riskLastUpdatedDateTime", default=None,)
	riskLevel: Optional[RiskLevel | str] = Field(alias="riskLevel", default=None,)
	riskState: Optional[RiskState | str] = Field(alias="riskState", default=None,)
	userDisplayName: Optional[str] = Field(alias="userDisplayName", default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName", default=None,)
	history: Optional[list[RiskyUserHistoryItem]] = Field(alias="history", default=None,)
	activity: Optional[RiskUserActivity] = Field(alias="activity", default=None,)
	initiatedBy: Optional[str] = Field(alias="initiatedBy", default=None,)
	userId: Optional[str] = Field(alias="userId", default=None,)

from .risk_detail import RiskDetail
from .risk_level import RiskLevel
from .risk_state import RiskState
from .risk_user_activity import RiskUserActivity

