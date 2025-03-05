from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CreatePostRequest(BaseModel):
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	manufacturer: Optional[str] = Field(alias="manufacturer",default=None,)
	model: Optional[str] = Field(alias="model",default=None,)
	physicalDeviceId: Optional[str] = Field(alias="physicalDeviceId",default=None,)
	hasPhysicalDevice: Optional[bool] = Field(alias="hasPhysicalDevice",default=None,)
	certificateSigningRequest: Optional[PrintCertificateSigningRequest] = Field(alias="certificateSigningRequest",default=None,)
	connectorId: Optional[str] = Field(alias="connectorId",default=None,)

from .print_certificate_signing_request import PrintCertificateSigningRequest

