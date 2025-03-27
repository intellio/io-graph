from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityWhoisContact(BaseModel):
	address: Optional[PhysicalAddress] = Field(alias="address", default=None,)
	email: Optional[str] = Field(alias="email", default=None,)
	fax: Optional[str] = Field(alias="fax", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	organization: Optional[str] = Field(alias="organization", default=None,)
	telephone: Optional[str] = Field(alias="telephone", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .physical_address import PhysicalAddress

