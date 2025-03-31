from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class AndroidManagedStoreAccountEnterpriseSettings(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.androidManagedStoreAccountEnterpriseSettings"] = Field(alias="@odata.type",)
	androidDeviceOwnerFullyManagedEnrollmentEnabled: Optional[bool] = Field(alias="androidDeviceOwnerFullyManagedEnrollmentEnabled", default=None,)
	bindStatus: Optional[AndroidManagedStoreAccountBindStatus | str] = Field(alias="bindStatus", default=None,)
	companyCodes: Optional[list[AndroidEnrollmentCompanyCode]] = Field(alias="companyCodes", default=None,)
	deviceOwnerManagementEnabled: Optional[bool] = Field(alias="deviceOwnerManagementEnabled", default=None,)
	enrollmentTarget: Optional[AndroidManagedStoreAccountEnrollmentTarget | str] = Field(alias="enrollmentTarget", default=None,)
	lastAppSyncDateTime: Optional[datetime] = Field(alias="lastAppSyncDateTime", default=None,)
	lastAppSyncStatus: Optional[AndroidManagedStoreAccountAppSyncStatus | str] = Field(alias="lastAppSyncStatus", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	managedGooglePlayInitialScopeTagIds: Optional[list[str]] = Field(alias="managedGooglePlayInitialScopeTagIds", default=None,)
	ownerOrganizationName: Optional[str] = Field(alias="ownerOrganizationName", default=None,)
	ownerUserPrincipalName: Optional[str] = Field(alias="ownerUserPrincipalName", default=None,)
	targetGroupIds: Optional[list[str]] = Field(alias="targetGroupIds", default=None,)

from .android_managed_store_account_bind_status import AndroidManagedStoreAccountBindStatus
from .android_enrollment_company_code import AndroidEnrollmentCompanyCode
from .android_managed_store_account_enrollment_target import AndroidManagedStoreAccountEnrollmentTarget
from .android_managed_store_account_app_sync_status import AndroidManagedStoreAccountAppSyncStatus
