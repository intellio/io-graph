from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field


class DeviceHealthScriptParameterCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[DeviceHealthScriptBooleanParameter, DeviceHealthScriptIntegerParameter, DeviceHealthScriptStringParameter],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .device_health_script_boolean_parameter import DeviceHealthScriptBooleanParameter
from .device_health_script_integer_parameter import DeviceHealthScriptIntegerParameter
from .device_health_script_string_parameter import DeviceHealthScriptStringParameter
