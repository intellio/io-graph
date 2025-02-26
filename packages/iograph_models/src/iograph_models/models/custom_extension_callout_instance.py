from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CustomExtensionCalloutInstance(BaseModel):
	customExtensionId: Optional[str] = Field(default=None,alias="customExtensionId",)
	detail: Optional[str] = Field(default=None,alias="detail",)
	externalCorrelationId: Optional[str] = Field(default=None,alias="externalCorrelationId",)
	id: Optional[str] = Field(default=None,alias="id",)
	status: Optional[CustomExtensionCalloutInstanceStatus] = Field(default=None,alias="status",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .custom_extension_callout_instance_status import CustomExtensionCalloutInstanceStatus

