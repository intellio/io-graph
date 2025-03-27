from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CompanyDetail(BaseModel):
	address: Optional[PhysicalAddress] = Field(alias="address", default=None,)
	companyCode: Optional[str] = Field(alias="companyCode", default=None,)
	department: Optional[str] = Field(alias="department", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	officeLocation: Optional[str] = Field(alias="officeLocation", default=None,)
	pronunciation: Optional[str] = Field(alias="pronunciation", default=None,)
	secondaryDepartment: Optional[str] = Field(alias="secondaryDepartment", default=None,)
	webUrl: Optional[str] = Field(alias="webUrl", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .physical_address import PhysicalAddress

