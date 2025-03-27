from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Template(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	deviceTemplates: Optional[list[DeviceTemplate]] = Field(alias="deviceTemplates", default=None,)

from .device_template import DeviceTemplate

