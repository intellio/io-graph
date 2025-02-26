from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecuritySslCertificateEntity(BaseModel):
	address: Optional[PhysicalAddress] = Field(default=None,alias="address",)
	alternateNames: list[Optional[str]] = Field(alias="alternateNames",)
	commonName: Optional[str] = Field(default=None,alias="commonName",)
	email: Optional[str] = Field(default=None,alias="email",)
	givenName: Optional[str] = Field(default=None,alias="givenName",)
	organizationName: Optional[str] = Field(default=None,alias="organizationName",)
	organizationUnitName: Optional[str] = Field(default=None,alias="organizationUnitName",)
	serialNumber: Optional[str] = Field(default=None,alias="serialNumber",)
	surname: Optional[str] = Field(default=None,alias="surname",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .physical_address import PhysicalAddress

