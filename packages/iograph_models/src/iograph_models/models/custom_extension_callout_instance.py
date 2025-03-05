from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CustomExtensionCalloutInstance(BaseModel):
	customExtensionId: Optional[str] = Field(alias="customExtensionId",default=None,)
	detail: Optional[str] = Field(alias="detail",default=None,)
	externalCorrelationId: Optional[str] = Field(alias="externalCorrelationId",default=None,)
	id: Optional[str] = Field(alias="id",default=None,)
	status: Optional[str | CustomExtensionCalloutInstanceStatus] = Field(alias="status",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .custom_extension_callout_instance_status import CustomExtensionCalloutInstanceStatus

