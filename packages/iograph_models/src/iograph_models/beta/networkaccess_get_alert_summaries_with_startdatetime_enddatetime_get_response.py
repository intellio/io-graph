from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Networkaccess_get_alert_summaries_with_startdatetime_enddatetimeGetResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[NetworkaccessAlertSummary]] = Field(alias="value", default=None,)

from .networkaccess_alert_summary import NetworkaccessAlertSummary
