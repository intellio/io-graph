from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class IndustryDataIndustryDataRunStatistics(BaseModel):
	activityStatistics: Optional[list[Annotated[Union[IndustryDataInboundActivityResults]],Field(discriminator="odata_type")]]] = Field(alias="activityStatistics", default=None,)
	inboundTotals: Optional[IndustryDataAggregatedInboundStatistics] = Field(alias="inboundTotals", default=None,)
	runId: Optional[str] = Field(alias="runId", default=None,)
	status: Optional[IndustryDataIndustryDataRunStatus | str] = Field(alias="status", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .industry_data_inbound_activity_results import IndustryDataInboundActivityResults
from .industry_data_aggregated_inbound_statistics import IndustryDataAggregatedInboundStatistics
from .industry_data_industry_data_run_status import IndustryDataIndustryDataRunStatus

