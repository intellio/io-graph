from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class CertificateConnectorDetails(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.certificateConnectorDetails"] = Field(alias="@odata.type",)
	connectorName: Optional[str] = Field(alias="connectorName", default=None,)
	connectorVersion: Optional[str] = Field(alias="connectorVersion", default=None,)
	enrollmentDateTime: Optional[datetime] = Field(alias="enrollmentDateTime", default=None,)
	lastCheckinDateTime: Optional[datetime] = Field(alias="lastCheckinDateTime", default=None,)
	machineName: Optional[str] = Field(alias="machineName", default=None,)

