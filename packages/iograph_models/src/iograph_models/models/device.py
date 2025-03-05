from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Device(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	deletedDateTime: Optional[datetime] = Field(default=None,alias="deletedDateTime",)
	accountEnabled: Optional[bool] = Field(default=None,alias="accountEnabled",)
	alternativeSecurityIds: Optional[list[AlternativeSecurityId]] = Field(default=None,alias="alternativeSecurityIds",)
	approximateLastSignInDateTime: Optional[datetime] = Field(default=None,alias="approximateLastSignInDateTime",)
	complianceExpirationDateTime: Optional[datetime] = Field(default=None,alias="complianceExpirationDateTime",)
	deviceCategory: Optional[str] = Field(default=None,alias="deviceCategory",)
	deviceId: Optional[str] = Field(default=None,alias="deviceId",)
	deviceMetadata: Optional[str] = Field(default=None,alias="deviceMetadata",)
	deviceOwnership: Optional[str] = Field(default=None,alias="deviceOwnership",)
	deviceVersion: Optional[int] = Field(default=None,alias="deviceVersion",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	enrollmentProfileName: Optional[str] = Field(default=None,alias="enrollmentProfileName",)
	enrollmentType: Optional[str] = Field(default=None,alias="enrollmentType",)
	isCompliant: Optional[bool] = Field(default=None,alias="isCompliant",)
	isManaged: Optional[bool] = Field(default=None,alias="isManaged",)
	isManagementRestricted: Optional[bool] = Field(default=None,alias="isManagementRestricted",)
	isRooted: Optional[bool] = Field(default=None,alias="isRooted",)
	managementType: Optional[str] = Field(default=None,alias="managementType",)
	manufacturer: Optional[str] = Field(default=None,alias="manufacturer",)
	mdmAppId: Optional[str] = Field(default=None,alias="mdmAppId",)
	model: Optional[str] = Field(default=None,alias="model",)
	onPremisesLastSyncDateTime: Optional[datetime] = Field(default=None,alias="onPremisesLastSyncDateTime",)
	onPremisesSecurityIdentifier: Optional[str] = Field(default=None,alias="onPremisesSecurityIdentifier",)
	onPremisesSyncEnabled: Optional[bool] = Field(default=None,alias="onPremisesSyncEnabled",)
	operatingSystem: Optional[str] = Field(default=None,alias="operatingSystem",)
	operatingSystemVersion: Optional[str] = Field(default=None,alias="operatingSystemVersion",)
	physicalIds: Optional[list[str]] = Field(default=None,alias="physicalIds",)
	profileType: Optional[str] = Field(default=None,alias="profileType",)
	registrationDateTime: Optional[datetime] = Field(default=None,alias="registrationDateTime",)
	systemLabels: Optional[list[str]] = Field(default=None,alias="systemLabels",)
	trustType: Optional[str] = Field(default=None,alias="trustType",)
	extensions: Optional[list[Extension]] = Field(default=None,alias="extensions",)
	memberOf: Optional[list[DirectoryObject]] = Field(default=None,alias="memberOf",)
	registeredOwners: Optional[list[DirectoryObject]] = Field(default=None,alias="registeredOwners",)
	registeredUsers: Optional[list[DirectoryObject]] = Field(default=None,alias="registeredUsers",)
	transitiveMemberOf: Optional[list[DirectoryObject]] = Field(default=None,alias="transitiveMemberOf",)

from .alternative_security_id import AlternativeSecurityId
from .extension import Extension
from .directory_object import DirectoryObject
from .directory_object import DirectoryObject
from .directory_object import DirectoryObject
from .directory_object import DirectoryObject

