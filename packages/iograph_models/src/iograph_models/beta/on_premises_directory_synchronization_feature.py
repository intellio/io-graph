from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OnPremisesDirectorySynchronizationFeature(BaseModel):
	blockCloudObjectTakeoverThroughHardMatchEnabled: Optional[bool] = Field(alias="blockCloudObjectTakeoverThroughHardMatchEnabled", default=None,)
	blockSoftMatchEnabled: Optional[bool] = Field(alias="blockSoftMatchEnabled", default=None,)
	bypassDirSyncOverridesEnabled: Optional[bool] = Field(alias="bypassDirSyncOverridesEnabled", default=None,)
	cloudPasswordPolicyForPasswordSyncedUsersEnabled: Optional[bool] = Field(alias="cloudPasswordPolicyForPasswordSyncedUsersEnabled", default=None,)
	concurrentCredentialUpdateEnabled: Optional[bool] = Field(alias="concurrentCredentialUpdateEnabled", default=None,)
	concurrentOrgIdProvisioningEnabled: Optional[bool] = Field(alias="concurrentOrgIdProvisioningEnabled", default=None,)
	deviceWritebackEnabled: Optional[bool] = Field(alias="deviceWritebackEnabled", default=None,)
	directoryExtensionsEnabled: Optional[bool] = Field(alias="directoryExtensionsEnabled", default=None,)
	fopeConflictResolutionEnabled: Optional[bool] = Field(alias="fopeConflictResolutionEnabled", default=None,)
	groupWriteBackEnabled: Optional[bool] = Field(alias="groupWriteBackEnabled", default=None,)
	passwordSyncEnabled: Optional[bool] = Field(alias="passwordSyncEnabled", default=None,)
	passwordWritebackEnabled: Optional[bool] = Field(alias="passwordWritebackEnabled", default=None,)
	quarantineUponProxyAddressesConflictEnabled: Optional[bool] = Field(alias="quarantineUponProxyAddressesConflictEnabled", default=None,)
	quarantineUponUpnConflictEnabled: Optional[bool] = Field(alias="quarantineUponUpnConflictEnabled", default=None,)
	softMatchOnUpnEnabled: Optional[bool] = Field(alias="softMatchOnUpnEnabled", default=None,)
	synchronizeUpnForManagedUsersEnabled: Optional[bool] = Field(alias="synchronizeUpnForManagedUsersEnabled", default=None,)
	unifiedGroupWritebackEnabled: Optional[bool] = Field(alias="unifiedGroupWritebackEnabled", default=None,)
	userForcePasswordChangeOnLogonEnabled: Optional[bool] = Field(alias="userForcePasswordChangeOnLogonEnabled", default=None,)
	userWritebackEnabled: Optional[bool] = Field(alias="userWritebackEnabled", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


