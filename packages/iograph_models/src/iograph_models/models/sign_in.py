from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SignIn(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	appDisplayName: Optional[str] = Field(default=None,alias="appDisplayName",)
	appId: Optional[str] = Field(default=None,alias="appId",)
	appliedConditionalAccessPolicies: Optional[list[AppliedConditionalAccessPolicy]] = Field(default=None,alias="appliedConditionalAccessPolicies",)
	clientAppUsed: Optional[str] = Field(default=None,alias="clientAppUsed",)
	conditionalAccessStatus: Optional[ConditionalAccessStatus] = Field(default=None,alias="conditionalAccessStatus",)
	correlationId: Optional[str] = Field(default=None,alias="correlationId",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	deviceDetail: Optional[DeviceDetail] = Field(default=None,alias="deviceDetail",)
	ipAddress: Optional[str] = Field(default=None,alias="ipAddress",)
	isInteractive: Optional[bool] = Field(default=None,alias="isInteractive",)
	location: Optional[SignInLocation] = Field(default=None,alias="location",)
	resourceDisplayName: Optional[str] = Field(default=None,alias="resourceDisplayName",)
	resourceId: Optional[str] = Field(default=None,alias="resourceId",)
	riskDetail: Optional[RiskDetail] = Field(default=None,alias="riskDetail",)
	riskEventTypes: Optional[RiskEventType] = Field(default=None,alias="riskEventTypes",)
	riskEventTypes_v2: Optional[list[str]] = Field(default=None,alias="riskEventTypes_v2",)
	riskLevelAggregated: Optional[RiskLevel] = Field(default=None,alias="riskLevelAggregated",)
	riskLevelDuringSignIn: Optional[RiskLevel] = Field(default=None,alias="riskLevelDuringSignIn",)
	riskState: Optional[RiskState] = Field(default=None,alias="riskState",)
	status: Optional[SignInStatus] = Field(default=None,alias="status",)
	userDisplayName: Optional[str] = Field(default=None,alias="userDisplayName",)
	userId: Optional[str] = Field(default=None,alias="userId",)
	userPrincipalName: Optional[str] = Field(default=None,alias="userPrincipalName",)

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

