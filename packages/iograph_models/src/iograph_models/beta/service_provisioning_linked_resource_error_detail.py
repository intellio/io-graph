from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ServiceProvisioningLinkedResourceErrorDetail(BaseModel):
	code: Optional[str] = Field(alias="code", default=None,)
	details: Optional[str] = Field(alias="details", default=None,)
	message: Optional[str] = Field(alias="message", default=None,)
	odata_type: Literal["#microsoft.graph.serviceProvisioningLinkedResourceErrorDetail"] = Field(alias="@odata.type", default="#microsoft.graph.serviceProvisioningLinkedResourceErrorDetail")
	propertyName: Optional[str] = Field(alias="propertyName", default=None,)
	target: Optional[str] = Field(alias="target", default=None,)

