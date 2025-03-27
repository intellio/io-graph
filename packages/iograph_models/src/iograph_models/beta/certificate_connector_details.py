from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class CertificateConnectorDetails(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	connectorName: Optional[str] = Field(alias="connectorName", default=None,)
	connectorVersion: Optional[str] = Field(alias="connectorVersion", default=None,)
	enrollmentDateTime: Optional[datetime] = Field(alias="enrollmentDateTime", default=None,)
	lastCheckinDateTime: Optional[datetime] = Field(alias="lastCheckinDateTime", default=None,)
	machineName: Optional[str] = Field(alias="machineName", default=None,)


