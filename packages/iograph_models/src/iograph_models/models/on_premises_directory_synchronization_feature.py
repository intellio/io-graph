from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OnPremisesDirectorySynchronizationFeature(BaseModel):
	blockCloudObjectTakeoverThroughHardMatchEnabled: Optional[bool] = Field(default=None,alias="blockCloudObjectTakeoverThroughHardMatchEnabled",)
	blockSoftMatchEnabled: Optional[bool] = Field(default=None,alias="blockSoftMatchEnabled",)
	bypassDirSyncOverridesEnabled: Optional[bool] = Field(default=None,alias="bypassDirSyncOverridesEnabled",)
	cloudPasswordPolicyForPasswordSyncedUsersEnabled: Optional[bool] = Field(default=None,alias="cloudPasswordPolicyForPasswordSyncedUsersEnabled",)
	concurrentCredentialUpdateEnabled: Optional[bool] = Field(default=None,alias="concurrentCredentialUpdateEnabled",)
	concurrentOrgIdProvisioningEnabled: Optional[bool] = Field(default=None,alias="concurrentOrgIdProvisioningEnabled",)
	deviceWritebackEnabled: Optional[bool] = Field(default=None,alias="deviceWritebackEnabled",)
	directoryExtensionsEnabled: Optional[bool] = Field(default=None,alias="directoryExtensionsEnabled",)
	fopeConflictResolutionEnabled: Optional[bool] = Field(default=None,alias="fopeConflictResolutionEnabled",)
	groupWriteBackEnabled: Optional[bool] = Field(default=None,alias="groupWriteBackEnabled",)
	passwordSyncEnabled: Optional[bool] = Field(default=None,alias="passwordSyncEnabled",)
	passwordWritebackEnabled: Optional[bool] = Field(default=None,alias="passwordWritebackEnabled",)
	quarantineUponProxyAddressesConflictEnabled: Optional[bool] = Field(default=None,alias="quarantineUponProxyAddressesConflictEnabled",)
	quarantineUponUpnConflictEnabled: Optional[bool] = Field(default=None,alias="quarantineUponUpnConflictEnabled",)
	softMatchOnUpnEnabled: Optional[bool] = Field(default=None,alias="softMatchOnUpnEnabled",)
	synchronizeUpnForManagedUsersEnabled: Optional[bool] = Field(default=None,alias="synchronizeUpnForManagedUsersEnabled",)
	unifiedGroupWritebackEnabled: Optional[bool] = Field(default=None,alias="unifiedGroupWritebackEnabled",)
	userForcePasswordChangeOnLogonEnabled: Optional[bool] = Field(default=None,alias="userForcePasswordChangeOnLogonEnabled",)
	userWritebackEnabled: Optional[bool] = Field(default=None,alias="userWritebackEnabled",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


