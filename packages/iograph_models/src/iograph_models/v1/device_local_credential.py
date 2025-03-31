from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class DeviceLocalCredential(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.deviceLocalCredential"] = Field(alias="@odata.type",)
	accountName: Optional[str] = Field(alias="accountName", default=None,)
	accountSid: Optional[str] = Field(alias="accountSid", default=None,)
	backupDateTime: Optional[datetime] = Field(alias="backupDateTime", default=None,)
	passwordBase64: Optional[str] = Field(alias="passwordBase64", default=None,)

