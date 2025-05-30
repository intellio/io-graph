from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class NetworkaccessAlertSummary(BaseModel):
	alertType: Optional[NetworkaccessAlertType | str] = Field(alias="alertType", default=None,)
	count: Optional[int] = Field(alias="count", default=None,)
	severity: Optional[NetworkaccessAlertSeverity | str] = Field(alias="severity", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .networkaccess_alert_type import NetworkaccessAlertType
from .networkaccess_alert_severity import NetworkaccessAlertSeverity
