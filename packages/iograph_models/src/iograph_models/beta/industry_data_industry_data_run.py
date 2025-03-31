from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field


class IndustryDataIndustryDataRun(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.industryData.industryDataRun"] = Field(alias="@odata.type",)
	blockingError: Optional[PublicError] = Field(alias="blockingError", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	endDateTime: Optional[datetime] = Field(alias="endDateTime", default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime", default=None,)
	status: Optional[IndustryDataIndustryDataRunStatus | str] = Field(alias="status", default=None,)
	activities: Optional[list[Annotated[Union[IndustryDataInboundFlowActivity, IndustryDataOutboundFlowActivity],Field(discriminator="odata_type")]]] = Field(alias="activities", default=None,)

from .public_error import PublicError
from .industry_data_industry_data_run_status import IndustryDataIndustryDataRunStatus
from .industry_data_inbound_flow_activity import IndustryDataInboundFlowActivity
from .industry_data_outbound_flow_activity import IndustryDataOutboundFlowActivity
