from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Networkaccess_get_destination_summaries_with_startdatetime_enddatetime_aggregatedbyGetResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[NetworkaccessDestinationSummary]] = Field(alias="value",default=None,)

from .networkaccess_destination_summary import NetworkaccessDestinationSummary

