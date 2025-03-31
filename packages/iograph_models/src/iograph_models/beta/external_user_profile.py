from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class ExternalUserProfile(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.externalUserProfile"] = Field(alias="@odata.type", default="#microsoft.graph.externalUserProfile")
	deletedDateTime: Optional[datetime] = Field(alias="deletedDateTime", default=None,)
	address: Optional[PhysicalOfficeAddress] = Field(alias="address", default=None,)
	companyName: Optional[str] = Field(alias="companyName", default=None,)
	createdBy: Optional[str] = Field(alias="createdBy", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	department: Optional[str] = Field(alias="department", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	isDiscoverable: Optional[bool] = Field(alias="isDiscoverable", default=None,)
	isEnabled: Optional[bool] = Field(alias="isEnabled", default=None,)
	jobTitle: Optional[str] = Field(alias="jobTitle", default=None,)
	phoneNumber: Optional[str] = Field(alias="phoneNumber", default=None,)
	supervisorId: Optional[str] = Field(alias="supervisorId", default=None,)

from .physical_office_address import PhysicalOfficeAddress
