from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class ServiceProvisioningXmlError(BaseModel):
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	isResolved: Optional[bool] = Field(alias="isResolved", default=None,)
	serviceInstance: Optional[str] = Field(alias="serviceInstance", default=None,)
	odata_type: Literal["#microsoft.graph.serviceProvisioningXmlError"] = Field(alias="@odata.type", default="#microsoft.graph.serviceProvisioningXmlError")
	errorDetail: Optional[str] = Field(alias="errorDetail", default=None,)

