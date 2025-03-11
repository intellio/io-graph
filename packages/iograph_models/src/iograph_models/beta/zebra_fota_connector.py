from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ZebraFotaConnector(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	enrollmentAuthorizationUrl: Optional[str] = Field(alias="enrollmentAuthorizationUrl",default=None,)
	enrollmentToken: Optional[str] = Field(alias="enrollmentToken",default=None,)
	fotaAppsApproved: Optional[bool] = Field(alias="fotaAppsApproved",default=None,)
	lastSyncDateTime: Optional[datetime] = Field(alias="lastSyncDateTime",default=None,)
	state: Optional[ZebraFotaConnectorState | str] = Field(alias="state",default=None,)

from .zebra_fota_connector_state import ZebraFotaConnectorState

