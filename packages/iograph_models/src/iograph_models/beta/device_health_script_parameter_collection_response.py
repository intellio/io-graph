from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceHealthScriptParameterCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: SerializeAsAny[Optional[list[DeviceHealthScriptParameter]]] = Field(alias="value",default=None,)

from .device_health_script_parameter import DeviceHealthScriptParameter

