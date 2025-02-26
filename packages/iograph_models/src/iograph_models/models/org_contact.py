from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class OrgContact(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	deletedDateTime: Optional[datetime] = Field(default=None,alias="deletedDateTime",)
	addresses: list[PhysicalOfficeAddress] = Field(alias="addresses",)
	companyName: Optional[str] = Field(default=None,alias="companyName",)
	department: Optional[str] = Field(default=None,alias="department",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	givenName: Optional[str] = Field(default=None,alias="givenName",)
	jobTitle: Optional[str] = Field(default=None,alias="jobTitle",)
	mail: Optional[str] = Field(default=None,alias="mail",)
	mailNickname: Optional[str] = Field(default=None,alias="mailNickname",)
	onPremisesLastSyncDateTime: Optional[datetime] = Field(default=None,alias="onPremisesLastSyncDateTime",)
	onPremisesProvisioningErrors: list[OnPremisesProvisioningError] = Field(alias="onPremisesProvisioningErrors",)
	onPremisesSyncEnabled: Optional[bool] = Field(default=None,alias="onPremisesSyncEnabled",)
	phones: list[Phone] = Field(alias="phones",)
	proxyAddresses: list[str] = Field(alias="proxyAddresses",)
	serviceProvisioningErrors: list[ServiceProvisioningError] = Field(alias="serviceProvisioningErrors",)
	surname: Optional[str] = Field(default=None,alias="surname",)
	directReports: list[DirectoryObject] = Field(alias="directReports",)
	manager: Optional[DirectoryObject] = Field(default=None,alias="manager",)
	memberOf: list[DirectoryObject] = Field(alias="memberOf",)
	transitiveMemberOf: list[DirectoryObject] = Field(alias="transitiveMemberOf",)

from .physical_office_address import PhysicalOfficeAddress
from .on_premises_provisioning_error import OnPremisesProvisioningError
from .phone import Phone
from .service_provisioning_error import ServiceProvisioningError
from .directory_object import DirectoryObject
from .directory_object import DirectoryObject
from .directory_object import DirectoryObject
from .directory_object import DirectoryObject

