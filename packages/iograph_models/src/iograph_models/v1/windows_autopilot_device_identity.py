from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class WindowsAutopilotDeviceIdentity(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.windowsAutopilotDeviceIdentity"] = Field(alias="@odata.type",)
	addressableUserName: Optional[str] = Field(alias="addressableUserName", default=None,)
	azureActiveDirectoryDeviceId: Optional[str] = Field(alias="azureActiveDirectoryDeviceId", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	enrollmentState: Optional[EnrollmentState | str] = Field(alias="enrollmentState", default=None,)
	groupTag: Optional[str] = Field(alias="groupTag", default=None,)
	lastContactedDateTime: Optional[datetime] = Field(alias="lastContactedDateTime", default=None,)
	managedDeviceId: Optional[str] = Field(alias="managedDeviceId", default=None,)
	manufacturer: Optional[str] = Field(alias="manufacturer", default=None,)
	model: Optional[str] = Field(alias="model", default=None,)
	productKey: Optional[str] = Field(alias="productKey", default=None,)
	purchaseOrderIdentifier: Optional[str] = Field(alias="purchaseOrderIdentifier", default=None,)
	resourceName: Optional[str] = Field(alias="resourceName", default=None,)
	serialNumber: Optional[str] = Field(alias="serialNumber", default=None,)
	skuNumber: Optional[str] = Field(alias="skuNumber", default=None,)
	systemFamily: Optional[str] = Field(alias="systemFamily", default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName", default=None,)

from .enrollment_state import EnrollmentState
