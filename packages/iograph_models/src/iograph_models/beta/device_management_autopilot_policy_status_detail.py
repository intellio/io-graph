from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class DeviceManagementAutopilotPolicyStatusDetail(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.deviceManagementAutopilotPolicyStatusDetail"] = Field(alias="@odata.type",)
	complianceStatus: Optional[DeviceManagementAutopilotPolicyComplianceStatus | str] = Field(alias="complianceStatus", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	errorCode: Optional[int] = Field(alias="errorCode", default=None,)
	lastReportedDateTime: Optional[datetime] = Field(alias="lastReportedDateTime", default=None,)
	policyType: Optional[DeviceManagementAutopilotPolicyType | str] = Field(alias="policyType", default=None,)
	trackedOnEnrollmentStatus: Optional[bool] = Field(alias="trackedOnEnrollmentStatus", default=None,)

from .device_management_autopilot_policy_compliance_status import DeviceManagementAutopilotPolicyComplianceStatus
from .device_management_autopilot_policy_type import DeviceManagementAutopilotPolicyType
