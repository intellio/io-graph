from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MacOSSoftwareUpdateStateSummaryCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[MacOSSoftwareUpdateStateSummary]] = Field(alias="value", default=None,)

from .mac_o_s_software_update_state_summary import MacOSSoftwareUpdateStateSummary

