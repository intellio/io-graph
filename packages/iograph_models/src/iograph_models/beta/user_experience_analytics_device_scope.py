from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class UserExperienceAnalyticsDeviceScope(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	deviceScopeName: Optional[str] = Field(alias="deviceScopeName",default=None,)
	enabled: Optional[bool] = Field(alias="enabled",default=None,)
	isBuiltIn: Optional[bool] = Field(alias="isBuiltIn",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	operator: Optional[DeviceScopeOperator | str] = Field(alias="operator",default=None,)
	ownerId: Optional[str] = Field(alias="ownerId",default=None,)
	parameter: Optional[DeviceScopeParameter | str] = Field(alias="parameter",default=None,)
	status: Optional[DeviceScopeStatus | str] = Field(alias="status",default=None,)
	value: Optional[str] = Field(alias="value",default=None,)
	valueObjectId: Optional[str] = Field(alias="valueObjectId",default=None,)

from .device_scope_operator import DeviceScopeOperator
from .device_scope_parameter import DeviceScopeParameter
from .device_scope_status import DeviceScopeStatus

