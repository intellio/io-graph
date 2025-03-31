from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class CertificateConnectorSetting(BaseModel):
	certExpiryTime: Optional[datetime] = Field(alias="certExpiryTime", default=None,)
	connectorVersion: Optional[str] = Field(alias="connectorVersion", default=None,)
	enrollmentError: Optional[str] = Field(alias="enrollmentError", default=None,)
	lastConnectorConnectionTime: Optional[datetime] = Field(alias="lastConnectorConnectionTime", default=None,)
	lastUploadVersion: Optional[int] = Field(alias="lastUploadVersion", default=None,)
	status: Optional[int] = Field(alias="status", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

