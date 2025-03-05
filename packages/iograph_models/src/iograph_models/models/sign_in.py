from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SignIn(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	appDisplayName: Optional[str] = Field(alias="appDisplayName",default=None,)
	appId: Optional[str] = Field(alias="appId",default=None,)
	appliedConditionalAccessPolicies: Optional[list[AppliedConditionalAccessPolicy]] = Field(alias="appliedConditionalAccessPolicies",default=None,)
	clientAppUsed: Optional[str] = Field(alias="clientAppUsed",default=None,)
	conditionalAccessStatus: Optional[str | ConditionalAccessStatus] = Field(alias="conditionalAccessStatus",default=None,)
	correlationId: Optional[str] = Field(alias="correlationId",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	deviceDetail: Optional[DeviceDetail] = Field(alias="deviceDetail",default=None,)
	ipAddress: Optional[str] = Field(alias="ipAddress",default=None,)
	isInteractive: Optional[bool] = Field(alias="isInteractive",default=None,)
	location: Optional[SignInLocation] = Field(alias="location",default=None,)
	resourceDisplayName: Optional[str] = Field(alias="resourceDisplayName",default=None,)
	resourceId: Optional[str] = Field(alias="resourceId",default=None,)
	riskDetail: Optional[str | RiskDetail] = Field(alias="riskDetail",default=None,)
	riskEventTypes: Optional[str | RiskEventType] = Field(alias="riskEventTypes",default=None,)
	riskEventTypes_v2: Optional[list[str]] = Field(alias="riskEventTypes_v2",default=None,)
	riskLevelAggregated: Optional[str | RiskLevel] = Field(alias="riskLevelAggregated",default=None,)
	riskLevelDuringSignIn: Optional[str | RiskLevel] = Field(alias="riskLevelDuringSignIn",default=None,)
	riskState: Optional[str | RiskState] = Field(alias="riskState",default=None,)
	status: Optional[SignInStatus] = Field(alias="status",default=None,)
	userDisplayName: Optional[str] = Field(alias="userDisplayName",default=None,)
	userId: Optional[str] = Field(alias="userId",default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName",default=None,)

from .applied_conditional_access_policy import AppliedConditionalAccessPolicy
from .conditional_access_status import ConditionalAccessStatus
from .device_detail import DeviceDetail
from .sign_in_location import SignInLocation
from .risk_detail import RiskDetail
from .risk_event_type import RiskEventType
from .risk_level import RiskLevel
from .risk_level import RiskLevel
from .risk_state import RiskState
from .sign_in_status import SignInStatus

