from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Networkaccess_get_alert_frequencies_with_startdatetime_enddatetimeGetResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[NetworkaccessAlertFrequencyPoint]] = Field(alias="value",default=None,)

from .networkaccess_alert_frequency_point import NetworkaccessAlertFrequencyPoint

