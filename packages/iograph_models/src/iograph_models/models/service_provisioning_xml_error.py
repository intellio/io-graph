from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ServiceProvisioningXmlError(BaseModel):
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	isResolved: Optional[bool] = Field(default=None,alias="isResolved",)
	serviceInstance: Optional[str] = Field(default=None,alias="serviceInstance",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	errorDetail: Optional[str] = Field(default=None,alias="errorDetail",)


