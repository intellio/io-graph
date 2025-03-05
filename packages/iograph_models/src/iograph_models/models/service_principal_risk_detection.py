from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ServicePrincipalRiskDetection(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	activity: Optional[ActivityType] = Field(default=None,alias="activity",)
	activityDateTime: Optional[datetime] = Field(default=None,alias="activityDateTime",)
	additionalInfo: Optional[str] = Field(default=None,alias="additionalInfo",)
	appId: Optional[str] = Field(default=None,alias="appId",)
	correlationId: Optional[str] = Field(default=None,alias="correlationId",)
	detectedDateTime: Optional[datetime] = Field(default=None,alias="detectedDateTime",)
	detectionTimingType: Optional[RiskDetectionTimingType] = Field(default=None,alias="detectionTimingType",)
	ipAddress: Optional[str] = Field(default=None,alias="ipAddress",)
	keyIds: Optional[list[str]] = Field(default=None,alias="keyIds",)
	lastUpdatedDateTime: Optional[datetime] = Field(default=None,alias="lastUpdatedDateTime",)
	location: Optional[SignInLocation] = Field(default=None,alias="location",)
	requestId: Optional[str] = Field(default=None,alias="requestId",)
	riskDetail: Optional[RiskDetail] = Field(default=None,alias="riskDetail",)
	riskEventType: Optional[str] = Field(default=None,alias="riskEventType",)
	riskLevel: Optional[RiskLevel] = Field(default=None,alias="riskLevel",)
	riskState: Optional[RiskState] = Field(default=None,alias="riskState",)
	servicePrincipalDisplayName: Optional[str] = Field(default=None,alias="servicePrincipalDisplayName",)
	servicePrincipalId: Optional[str] = Field(default=None,alias="servicePrincipalId",)
	source: Optional[str] = Field(default=None,alias="source",)
	tokenIssuerType: Optional[TokenIssuerType] = Field(default=None,alias="tokenIssuerType",)

from .activity_type import ActivityType
from .risk_detection_timing_type import RiskDetectionTimingType
from .sign_in_location import SignInLocation
from .risk_detail import RiskDetail
from .risk_level import RiskLevel
from .risk_state import RiskState
from .token_issuer_type import TokenIssuerType

