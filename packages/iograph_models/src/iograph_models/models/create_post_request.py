from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CreatePostRequest(BaseModel):
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	manufacturer: Optional[str] = Field(default=None,alias="manufacturer",)
	model: Optional[str] = Field(default=None,alias="model",)
	physicalDeviceId: Optional[str] = Field(default=None,alias="physicalDeviceId",)
	hasPhysicalDevice: Optional[bool] = Field(default=None,alias="hasPhysicalDevice",)
	certificateSigningRequest: Optional[PrintCertificateSigningRequest] = Field(default=None,alias="certificateSigningRequest",)
	connectorId: Optional[str] = Field(default=None,alias="connectorId",)

from .print_certificate_signing_request import PrintCertificateSigningRequest

