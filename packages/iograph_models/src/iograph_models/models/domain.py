from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Domain(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	authenticationType: Optional[str] = Field(default=None,alias="authenticationType",)
	availabilityStatus: Optional[str] = Field(default=None,alias="availabilityStatus",)
	isAdminManaged: Optional[bool] = Field(default=None,alias="isAdminManaged",)
	isDefault: Optional[bool] = Field(default=None,alias="isDefault",)
	isInitial: Optional[bool] = Field(default=None,alias="isInitial",)
	isRoot: Optional[bool] = Field(default=None,alias="isRoot",)
	isVerified: Optional[bool] = Field(default=None,alias="isVerified",)
	manufacturer: Optional[str] = Field(default=None,alias="manufacturer",)
	model: Optional[str] = Field(default=None,alias="model",)
	passwordNotificationWindowInDays: Optional[int] = Field(default=None,alias="passwordNotificationWindowInDays",)
	passwordValidityPeriodInDays: Optional[int] = Field(default=None,alias="passwordValidityPeriodInDays",)
	state: Optional[DomainState] = Field(default=None,alias="state",)
	supportedServices: Optional[list[str]] = Field(default=None,alias="supportedServices",)
	domainNameReferences: SerializeAsAny[Optional[list[DirectoryObject]]] = Field(default=None,alias="domainNameReferences",)
	federationConfiguration: Optional[list[InternalDomainFederation]] = Field(default=None,alias="federationConfiguration",)
	rootDomain: Optional[Domain] = Field(default=None,alias="rootDomain",)
	serviceConfigurationRecords: SerializeAsAny[Optional[list[DomainDnsRecord]]] = Field(default=None,alias="serviceConfigurationRecords",)
	verificationDnsRecords: SerializeAsAny[Optional[list[DomainDnsRecord]]] = Field(default=None,alias="verificationDnsRecords",)

from .domain_state import DomainState
from .directory_object import DirectoryObject
from .internal_domain_federation import InternalDomainFederation
from .domain_dns_record import DomainDnsRecord
from .domain_dns_record import DomainDnsRecord

