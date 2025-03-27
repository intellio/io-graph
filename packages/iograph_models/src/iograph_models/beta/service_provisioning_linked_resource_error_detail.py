from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ServiceProvisioningLinkedResourceErrorDetail(BaseModel):
	code: Optional[str] = Field(alias="code", default=None,)
	details: Optional[str] = Field(alias="details", default=None,)
	message: Optional[str] = Field(alias="message", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	propertyName: Optional[str] = Field(alias="propertyName", default=None,)
	target: Optional[str] = Field(alias="target", default=None,)


