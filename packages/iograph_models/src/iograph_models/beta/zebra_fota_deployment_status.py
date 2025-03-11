from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ZebraFotaDeploymentStatus(BaseModel):
	cancelRequested: Optional[bool] = Field(alias="cancelRequested",default=None,)
	completeOrCanceledDateTime: Optional[datetime] = Field(alias="completeOrCanceledDateTime",default=None,)
	errorCode: Optional[ZebraFotaErrorCode | str] = Field(alias="errorCode",default=None,)
	lastUpdatedDateTime: Optional[datetime] = Field(alias="lastUpdatedDateTime",default=None,)
	state: Optional[ZebraFotaDeploymentState | str] = Field(alias="state",default=None,)
	totalAwaitingInstall: Optional[int] = Field(alias="totalAwaitingInstall",default=None,)
	totalCanceled: Optional[int] = Field(alias="totalCanceled",default=None,)
	totalCreated: Optional[int] = Field(alias="totalCreated",default=None,)
	totalDevices: Optional[int] = Field(alias="totalDevices",default=None,)
	totalDownloading: Optional[int] = Field(alias="totalDownloading",default=None,)
	totalFailedDownload: Optional[int] = Field(alias="totalFailedDownload",default=None,)
	totalFailedInstall: Optional[int] = Field(alias="totalFailedInstall",default=None,)
	totalScheduled: Optional[int] = Field(alias="totalScheduled",default=None,)
	totalSucceededInstall: Optional[int] = Field(alias="totalSucceededInstall",default=None,)
	totalUnknown: Optional[int] = Field(alias="totalUnknown",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .zebra_fota_error_code import ZebraFotaErrorCode
from .zebra_fota_deployment_state import ZebraFotaDeploymentState

