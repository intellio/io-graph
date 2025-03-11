from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class CertificateConnectorHealthMetricValue(BaseModel):
	dateTime: Optional[datetime] = Field(alias="dateTime",default=None,)
	failureCount: Optional[int] = Field(alias="failureCount",default=None,)
	successCount: Optional[int] = Field(alias="successCount",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


