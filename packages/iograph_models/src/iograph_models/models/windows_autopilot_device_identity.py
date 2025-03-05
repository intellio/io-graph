from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsAutopilotDeviceIdentity(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	addressableUserName: Optional[str] = Field(default=None,alias="addressableUserName",)
	azureActiveDirectoryDeviceId: Optional[str] = Field(default=None,alias="azureActiveDirectoryDeviceId",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	enrollmentState: Optional[EnrollmentState] = Field(default=None,alias="enrollmentState",)
	groupTag: Optional[str] = Field(default=None,alias="groupTag",)
	lastContactedDateTime: Optional[datetime] = Field(default=None,alias="lastContactedDateTime",)
	managedDeviceId: Optional[str] = Field(default=None,alias="managedDeviceId",)
	manufacturer: Optional[str] = Field(default=None,alias="manufacturer",)
	model: Optional[str] = Field(default=None,alias="model",)
	productKey: Optional[str] = Field(default=None,alias="productKey",)
	purchaseOrderIdentifier: Optional[str] = Field(default=None,alias="purchaseOrderIdentifier",)
	resourceName: Optional[str] = Field(default=None,alias="resourceName",)
	serialNumber: Optional[str] = Field(default=None,alias="serialNumber",)
	skuNumber: Optional[str] = Field(default=None,alias="skuNumber",)
	systemFamily: Optional[str] = Field(default=None,alias="systemFamily",)
	userPrincipalName: Optional[str] = Field(default=None,alias="userPrincipalName",)

from .enrollment_state import EnrollmentState

