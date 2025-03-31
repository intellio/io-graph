from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class Template(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.template"] = Field(alias="@odata.type",)
	deviceTemplates: Optional[list[DeviceTemplate]] = Field(alias="deviceTemplates", default=None,)

from .device_template import DeviceTemplate
