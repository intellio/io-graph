from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsDefenderApplicationControlSupplementalPolicyDeploymentStatus(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	deploymentStatus: Optional[WindowsDefenderApplicationControlSupplementalPolicyStatuses | str] = Field(alias="deploymentStatus",default=None,)
	deviceId: Optional[str] = Field(alias="deviceId",default=None,)
	deviceName: Optional[str] = Field(alias="deviceName",default=None,)
	lastSyncDateTime: Optional[datetime] = Field(alias="lastSyncDateTime",default=None,)
	osDescription: Optional[str] = Field(alias="osDescription",default=None,)
	osVersion: Optional[str] = Field(alias="osVersion",default=None,)
	policyVersion: Optional[str] = Field(alias="policyVersion",default=None,)
	userName: Optional[str] = Field(alias="userName",default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName",default=None,)
	policy: Optional[WindowsDefenderApplicationControlSupplementalPolicy] = Field(alias="policy",default=None,)

from .windows_defender_application_control_supplemental_policy_statuses import WindowsDefenderApplicationControlSupplementalPolicyStatuses
from .windows_defender_application_control_supplemental_policy import WindowsDefenderApplicationControlSupplementalPolicy

