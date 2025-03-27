from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsInformationProtectionDataRecoveryCertificate(BaseModel):
	certificate: Optional[str] = Field(alias="certificate", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	expirationDateTime: Optional[datetime] = Field(alias="expirationDateTime", default=None,)
	subjectName: Optional[str] = Field(alias="subjectName", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


