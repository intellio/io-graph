from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class OrgContact(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	deletedDateTime: Optional[datetime] = Field(default=None,alias="deletedDateTime",)
	addresses: Optional[list[PhysicalOfficeAddress]] = Field(default=None,alias="addresses",)
	companyName: Optional[str] = Field(default=None,alias="companyName",)
	department: Optional[str] = Field(default=None,alias="department",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	givenName: Optional[str] = Field(default=None,alias="givenName",)
	jobTitle: Optional[str] = Field(default=None,alias="jobTitle",)
	mail: Optional[str] = Field(default=None,alias="mail",)
	mailNickname: Optional[str] = Field(default=None,alias="mailNickname",)
	onPremisesLastSyncDateTime: Optional[datetime] = Field(default=None,alias="onPremisesLastSyncDateTime",)
	onPremisesProvisioningErrors: Optional[list[OnPremisesProvisioningError]] = Field(default=None,alias="onPremisesProvisioningErrors",)
	onPremisesSyncEnabled: Optional[bool] = Field(default=None,alias="onPremisesSyncEnabled",)
	phones: Optional[list[Phone]] = Field(default=None,alias="phones",)
	proxyAddresses: Optional[list[str]] = Field(default=None,alias="proxyAddresses",)
	serviceProvisioningErrors: SerializeAsAny[Optional[list[ServiceProvisioningError]]] = Field(default=None,alias="serviceProvisioningErrors",)
	surname: Optional[str] = Field(default=None,alias="surname",)
	directReports: SerializeAsAny[Optional[list[DirectoryObject]]] = Field(default=None,alias="directReports",)
	manager: SerializeAsAny[Optional[DirectoryObject]] = Field(default=None,alias="manager",)
	memberOf: SerializeAsAny[Optional[list[DirectoryObject]]] = Field(default=None,alias="memberOf",)
	transitiveMemberOf: SerializeAsAny[Optional[list[DirectoryObject]]] = Field(default=None,alias="transitiveMemberOf",)

from .physical_office_address import PhysicalOfficeAddress
from .on_premises_provisioning_error import OnPremisesProvisioningError
from .phone import Phone
from .service_provisioning_error import ServiceProvisioningError
from .directory_object import DirectoryObject
from .directory_object import DirectoryObject
from .directory_object import DirectoryObject
from .directory_object import DirectoryObject

