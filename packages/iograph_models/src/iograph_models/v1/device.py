from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Device(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	deletedDateTime: Optional[datetime] = Field(alias="deletedDateTime",default=None,)
	accountEnabled: Optional[bool] = Field(alias="accountEnabled",default=None,)
	alternativeSecurityIds: Optional[list[AlternativeSecurityId]] = Field(alias="alternativeSecurityIds",default=None,)
	approximateLastSignInDateTime: Optional[datetime] = Field(alias="approximateLastSignInDateTime",default=None,)
	complianceExpirationDateTime: Optional[datetime] = Field(alias="complianceExpirationDateTime",default=None,)
	deviceCategory: Optional[str] = Field(alias="deviceCategory",default=None,)
	deviceId: Optional[str] = Field(alias="deviceId",default=None,)
	deviceMetadata: Optional[str] = Field(alias="deviceMetadata",default=None,)
	deviceOwnership: Optional[str] = Field(alias="deviceOwnership",default=None,)
	deviceVersion: Optional[int] = Field(alias="deviceVersion",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	enrollmentProfileName: Optional[str] = Field(alias="enrollmentProfileName",default=None,)
	enrollmentType: Optional[str] = Field(alias="enrollmentType",default=None,)
	isCompliant: Optional[bool] = Field(alias="isCompliant",default=None,)
	isManaged: Optional[bool] = Field(alias="isManaged",default=None,)
	isManagementRestricted: Optional[bool] = Field(alias="isManagementRestricted",default=None,)
	isRooted: Optional[bool] = Field(alias="isRooted",default=None,)
	managementType: Optional[str] = Field(alias="managementType",default=None,)
	manufacturer: Optional[str] = Field(alias="manufacturer",default=None,)
	mdmAppId: Optional[str] = Field(alias="mdmAppId",default=None,)
	model: Optional[str] = Field(alias="model",default=None,)
	onPremisesLastSyncDateTime: Optional[datetime] = Field(alias="onPremisesLastSyncDateTime",default=None,)
	onPremisesSecurityIdentifier: Optional[str] = Field(alias="onPremisesSecurityIdentifier",default=None,)
	onPremisesSyncEnabled: Optional[bool] = Field(alias="onPremisesSyncEnabled",default=None,)
	operatingSystem: Optional[str] = Field(alias="operatingSystem",default=None,)
	operatingSystemVersion: Optional[str] = Field(alias="operatingSystemVersion",default=None,)
	physicalIds: Optional[list[str]] = Field(alias="physicalIds",default=None,)
	profileType: Optional[str] = Field(alias="profileType",default=None,)
	registrationDateTime: Optional[datetime] = Field(alias="registrationDateTime",default=None,)
	systemLabels: Optional[list[str]] = Field(alias="systemLabels",default=None,)
	trustType: Optional[str] = Field(alias="trustType",default=None,)
	extensions: SerializeAsAny[Optional[list[Extension]]] = Field(alias="extensions",default=None,)
	memberOf: SerializeAsAny[Optional[list[DirectoryObject]]] = Field(alias="memberOf",default=None,)
	registeredOwners: SerializeAsAny[Optional[list[DirectoryObject]]] = Field(alias="registeredOwners",default=None,)
	registeredUsers: SerializeAsAny[Optional[list[DirectoryObject]]] = Field(alias="registeredUsers",default=None,)
	transitiveMemberOf: SerializeAsAny[Optional[list[DirectoryObject]]] = Field(alias="transitiveMemberOf",default=None,)

from .alternative_security_id import AlternativeSecurityId
from .extension import Extension
from .directory_object import DirectoryObject
from .directory_object import DirectoryObject
from .directory_object import DirectoryObject
from .directory_object import DirectoryObject

