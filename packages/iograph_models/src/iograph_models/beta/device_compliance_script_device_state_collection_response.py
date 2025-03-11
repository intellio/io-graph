from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceComplianceScriptDeviceStateCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[DeviceComplianceScriptDeviceState]] = Field(alias="value",default=None,)

from .device_compliance_script_device_state import DeviceComplianceScriptDeviceState

