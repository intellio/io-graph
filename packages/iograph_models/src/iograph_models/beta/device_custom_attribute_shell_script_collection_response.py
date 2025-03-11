from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceCustomAttributeShellScriptCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[DeviceCustomAttributeShellScript]] = Field(alias="value",default=None,)

from .device_custom_attribute_shell_script import DeviceCustomAttributeShellScript

