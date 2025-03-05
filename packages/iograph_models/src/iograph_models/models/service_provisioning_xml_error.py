from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ServiceProvisioningXmlError(BaseModel):
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	isResolved: Optional[bool] = Field(alias="isResolved",default=None,)
	serviceInstance: Optional[str] = Field(alias="serviceInstance",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	errorDetail: Optional[str] = Field(alias="errorDetail",default=None,)


