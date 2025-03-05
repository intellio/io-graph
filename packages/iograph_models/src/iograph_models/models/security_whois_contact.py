from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityWhoisContact(BaseModel):
	address: Optional[PhysicalAddress] = Field(default=None,alias="address",)
	email: Optional[str] = Field(default=None,alias="email",)
	fax: Optional[str] = Field(default=None,alias="fax",)
	name: Optional[str] = Field(default=None,alias="name",)
	organization: Optional[str] = Field(default=None,alias="organization",)
	telephone: Optional[str] = Field(default=None,alias="telephone",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .physical_address import PhysicalAddress

