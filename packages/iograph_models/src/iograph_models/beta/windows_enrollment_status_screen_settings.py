from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsEnrollmentStatusScreenSettings(BaseModel):
	allowDeviceUseBeforeProfileAndAppInstallComplete: Optional[bool] = Field(alias="allowDeviceUseBeforeProfileAndAppInstallComplete", default=None,)
	allowDeviceUseOnInstallFailure: Optional[bool] = Field(alias="allowDeviceUseOnInstallFailure", default=None,)
	allowLogCollectionOnInstallFailure: Optional[bool] = Field(alias="allowLogCollectionOnInstallFailure", default=None,)
	blockDeviceSetupRetryByUser: Optional[bool] = Field(alias="blockDeviceSetupRetryByUser", default=None,)
	customErrorMessage: Optional[str] = Field(alias="customErrorMessage", default=None,)
	hideInstallationProgress: Optional[bool] = Field(alias="hideInstallationProgress", default=None,)
	installProgressTimeoutInMinutes: Optional[int] = Field(alias="installProgressTimeoutInMinutes", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


