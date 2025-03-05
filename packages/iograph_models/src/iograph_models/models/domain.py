from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Domain(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	authenticationType: Optional[str] = Field(alias="authenticationType",default=None,)
	availabilityStatus: Optional[str] = Field(alias="availabilityStatus",default=None,)
	isAdminManaged: Optional[bool] = Field(alias="isAdminManaged",default=None,)
	isDefault: Optional[bool] = Field(alias="isDefault",default=None,)
	isInitial: Optional[bool] = Field(alias="isInitial",default=None,)
	isRoot: Optional[bool] = Field(alias="isRoot",default=None,)
	isVerified: Optional[bool] = Field(alias="isVerified",default=None,)
	manufacturer: Optional[str] = Field(alias="manufacturer",default=None,)
	model: Optional[str] = Field(alias="model",default=None,)
	passwordNotificationWindowInDays: Optional[int] = Field(alias="passwordNotificationWindowInDays",default=None,)
	passwordValidityPeriodInDays: Optional[int] = Field(alias="passwordValidityPeriodInDays",default=None,)
	state: Optional[DomainState] = Field(alias="state",default=None,)
	supportedServices: Optional[list[str]] = Field(alias="supportedServices",default=None,)
	domainNameReferences: SerializeAsAny[Optional[list[DirectoryObject]]] = Field(alias="domainNameReferences",default=None,)
	federationConfiguration: Optional[list[InternalDomainFederation]] = Field(alias="federationConfiguration",default=None,)
	rootDomain: Optional[Domain] = Field(alias="rootDomain",default=None,)
	serviceConfigurationRecords: SerializeAsAny[Optional[list[DomainDnsRecord]]] = Field(alias="serviceConfigurationRecords",default=None,)
	verificationDnsRecords: SerializeAsAny[Optional[list[DomainDnsRecord]]] = Field(alias="verificationDnsRecords",default=None,)

from .domain_state import DomainState
from .directory_object import DirectoryObject
from .internal_domain_federation import InternalDomainFederation
from .domain_dns_record import DomainDnsRecord
from .domain_dns_record import DomainDnsRecord

