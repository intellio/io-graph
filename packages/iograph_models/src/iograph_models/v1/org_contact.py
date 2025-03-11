from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class OrgContact(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	deletedDateTime: Optional[datetime] = Field(alias="deletedDateTime",default=None,)
	addresses: Optional[list[PhysicalOfficeAddress]] = Field(alias="addresses",default=None,)
	companyName: Optional[str] = Field(alias="companyName",default=None,)
	department: Optional[str] = Field(alias="department",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	givenName: Optional[str] = Field(alias="givenName",default=None,)
	jobTitle: Optional[str] = Field(alias="jobTitle",default=None,)
	mail: Optional[str] = Field(alias="mail",default=None,)
	mailNickname: Optional[str] = Field(alias="mailNickname",default=None,)
	onPremisesLastSyncDateTime: Optional[datetime] = Field(alias="onPremisesLastSyncDateTime",default=None,)
	onPremisesProvisioningErrors: Optional[list[OnPremisesProvisioningError]] = Field(alias="onPremisesProvisioningErrors",default=None,)
	onPremisesSyncEnabled: Optional[bool] = Field(alias="onPremisesSyncEnabled",default=None,)
	phones: Optional[list[Phone]] = Field(alias="phones",default=None,)
	proxyAddresses: Optional[list[str]] = Field(alias="proxyAddresses",default=None,)
	serviceProvisioningErrors: SerializeAsAny[Optional[list[ServiceProvisioningError]]] = Field(alias="serviceProvisioningErrors",default=None,)
	surname: Optional[str] = Field(alias="surname",default=None,)
	directReports: SerializeAsAny[Optional[list[DirectoryObject]]] = Field(alias="directReports",default=None,)
	manager: SerializeAsAny[Optional[DirectoryObject]] = Field(alias="manager",default=None,)
	memberOf: SerializeAsAny[Optional[list[DirectoryObject]]] = Field(alias="memberOf",default=None,)
	transitiveMemberOf: SerializeAsAny[Optional[list[DirectoryObject]]] = Field(alias="transitiveMemberOf",default=None,)

from .physical_office_address import PhysicalOfficeAddress
from .on_premises_provisioning_error import OnPremisesProvisioningError
from .phone import Phone
from .service_provisioning_error import ServiceProvisioningError
from .directory_object import DirectoryObject
from .directory_object import DirectoryObject
from .directory_object import DirectoryObject
from .directory_object import DirectoryObject

