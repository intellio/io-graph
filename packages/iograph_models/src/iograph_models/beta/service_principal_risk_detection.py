from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ServicePrincipalRiskDetection(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	activity: Optional[ActivityType | str] = Field(alias="activity",default=None,)
	activityDateTime: Optional[datetime] = Field(alias="activityDateTime",default=None,)
	additionalInfo: Optional[str] = Field(alias="additionalInfo",default=None,)
	appId: Optional[str] = Field(alias="appId",default=None,)
	correlationId: Optional[str] = Field(alias="correlationId",default=None,)
	detectedDateTime: Optional[datetime] = Field(alias="detectedDateTime",default=None,)
	detectionTimingType: Optional[RiskDetectionTimingType | str] = Field(alias="detectionTimingType",default=None,)
	ipAddress: Optional[str] = Field(alias="ipAddress",default=None,)
	keyIds: Optional[list[str]] = Field(alias="keyIds",default=None,)
	lastUpdatedDateTime: Optional[datetime] = Field(alias="lastUpdatedDateTime",default=None,)
	location: Optional[SignInLocation] = Field(alias="location",default=None,)
	mitreTechniqueId: Optional[str] = Field(alias="mitreTechniqueId",default=None,)
	requestId: Optional[str] = Field(alias="requestId",default=None,)
	riskDetail: Optional[RiskDetail | str] = Field(alias="riskDetail",default=None,)
	riskEventType: Optional[str] = Field(alias="riskEventType",default=None,)
	riskLevel: Optional[RiskLevel | str] = Field(alias="riskLevel",default=None,)
	riskState: Optional[RiskState | str] = Field(alias="riskState",default=None,)
	servicePrincipalDisplayName: Optional[str] = Field(alias="servicePrincipalDisplayName",default=None,)
	servicePrincipalId: Optional[str] = Field(alias="servicePrincipalId",default=None,)
	source: Optional[str] = Field(alias="source",default=None,)
	tokenIssuerType: Optional[TokenIssuerType | str] = Field(alias="tokenIssuerType",default=None,)

from .activity_type import ActivityType
from .risk_detection_timing_type import RiskDetectionTimingType
from .sign_in_location import SignInLocation
from .risk_detail import RiskDetail
from .risk_level import RiskLevel
from .risk_state import RiskState
from .token_issuer_type import TokenIssuerType

