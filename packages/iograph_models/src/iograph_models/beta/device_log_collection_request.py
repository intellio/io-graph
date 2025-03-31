from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DeviceLogCollectionRequest(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	templateType: Optional[DeviceLogCollectionTemplateType | str] = Field(alias="templateType", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .device_log_collection_template_type import DeviceLogCollectionTemplateType
