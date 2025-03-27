from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class CloudPcReviewStatus(BaseModel):
	accessTier: Optional[CloudPcBlobAccessTier | str] = Field(alias="accessTier", default=None,)
	azureStorageAccountId: Optional[str] = Field(alias="azureStorageAccountId", default=None,)
	azureStorageAccountName: Optional[str] = Field(alias="azureStorageAccountName", default=None,)
	azureStorageContainerName: Optional[str] = Field(alias="azureStorageContainerName", default=None,)
	inReview: Optional[bool] = Field(alias="inReview", default=None,)
	restorePointDateTime: Optional[datetime] = Field(alias="restorePointDateTime", default=None,)
	reviewStartDateTime: Optional[datetime] = Field(alias="reviewStartDateTime", default=None,)
	subscriptionId: Optional[str] = Field(alias="subscriptionId", default=None,)
	subscriptionName: Optional[str] = Field(alias="subscriptionName", default=None,)
	userAccessLevel: Optional[CloudPcUserAccessLevel | str] = Field(alias="userAccessLevel", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .cloud_pc_blob_access_tier import CloudPcBlobAccessTier
from .cloud_pc_user_access_level import CloudPcUserAccessLevel

