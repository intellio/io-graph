from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecuritySslCertificateEntity(BaseModel):
	address: Optional[PhysicalAddress] = Field(alias="address", default=None,)
	alternateNames: Optional[list[str]] = Field(alias="alternateNames", default=None,)
	commonName: Optional[str] = Field(alias="commonName", default=None,)
	email: Optional[str] = Field(alias="email", default=None,)
	givenName: Optional[str] = Field(alias="givenName", default=None,)
	organizationName: Optional[str] = Field(alias="organizationName", default=None,)
	organizationUnitName: Optional[str] = Field(alias="organizationUnitName", default=None,)
	serialNumber: Optional[str] = Field(alias="serialNumber", default=None,)
	surname: Optional[str] = Field(alias="surname", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .physical_address import PhysicalAddress
