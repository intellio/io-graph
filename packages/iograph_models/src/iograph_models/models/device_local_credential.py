from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class DeviceLocalCredential(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	accountName: Optional[str] = Field(default=None,alias="accountName",)
	accountSid: Optional[str] = Field(default=None,alias="accountSid",)
	backupDateTime: Optional[datetime] = Field(default=None,alias="backupDateTime",)
	passwordBase64: Optional[str] = Field(default=None,alias="passwordBase64",)


