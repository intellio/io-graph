from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AppsAndServicesSettings(BaseModel):
	isAppAndServicesTrialEnabled: Optional[bool] = Field(alias="isAppAndServicesTrialEnabled", default=None,)
	isOfficeStoreEnabled: Optional[bool] = Field(alias="isOfficeStoreEnabled", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

