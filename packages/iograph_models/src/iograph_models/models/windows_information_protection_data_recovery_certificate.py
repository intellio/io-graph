from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class WindowsInformationProtectionDataRecoveryCertificate(BaseModel):
	certificate: Optional[str] = Field(default=None,alias="certificate",)
	description: Optional[str] = Field(default=None,alias="description",)
	expirationDateTime: Optional[datetime] = Field(default=None,alias="expirationDateTime",)
	subjectName: Optional[str] = Field(default=None,alias="subjectName",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


