from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class PrivilegeManagementElevation(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	certificatePayload: Optional[str] = Field(alias="certificatePayload",default=None,)
	companyName: Optional[str] = Field(alias="companyName",default=None,)
	deviceId: Optional[str] = Field(alias="deviceId",default=None,)
	deviceName: Optional[str] = Field(alias="deviceName",default=None,)
	elevationType: Optional[PrivilegeManagementElevationType | str] = Field(alias="elevationType",default=None,)
	eventDateTime: Optional[datetime] = Field(alias="eventDateTime",default=None,)
	fileDescription: Optional[str] = Field(alias="fileDescription",default=None,)
	filePath: Optional[str] = Field(alias="filePath",default=None,)
	fileVersion: Optional[str] = Field(alias="fileVersion",default=None,)
	hash: Optional[str] = Field(alias="hash",default=None,)
	internalName: Optional[str] = Field(alias="internalName",default=None,)
	justification: Optional[str] = Field(alias="justification",default=None,)
	parentProcessName: Optional[str] = Field(alias="parentProcessName",default=None,)
	policyId: Optional[str] = Field(alias="policyId",default=None,)
	policyName: Optional[str] = Field(alias="policyName",default=None,)
	processType: Optional[PrivilegeManagementProcessType | str] = Field(alias="processType",default=None,)
	productName: Optional[str] = Field(alias="productName",default=None,)
	result: Optional[int] = Field(alias="result",default=None,)
	ruleId: Optional[str] = Field(alias="ruleId",default=None,)
	systemInitiatedElevation: Optional[bool] = Field(alias="systemInitiatedElevation",default=None,)
	upn: Optional[str] = Field(alias="upn",default=None,)
	userType: Optional[PrivilegeManagementEndUserType | str] = Field(alias="userType",default=None,)

from .privilege_management_elevation_type import PrivilegeManagementElevationType
from .privilege_management_process_type import PrivilegeManagementProcessType
from .privilege_management_end_user_type import PrivilegeManagementEndUserType

