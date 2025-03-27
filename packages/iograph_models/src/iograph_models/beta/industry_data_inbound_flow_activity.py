from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class IndustryDataInboundFlowActivity(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.industryData.inboundFlowActivity"] = Field(alias="@odata.type", default="#microsoft.graph.industryData.inboundFlowActivity")
	blockingError: Optional[PublicError] = Field(alias="blockingError", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	status: Optional[IndustryDataIndustryDataActivityStatus | str] = Field(alias="status", default=None,)
	activity: Optional[Union[IndustryDataInboundFlow, IndustryDataInboundApiFlow, IndustryDataInboundFileFlow]] = Field(alias="activity", default=None,discriminator="odata_type", )

from .public_error import PublicError
from .industry_data_industry_data_activity_status import IndustryDataIndustryDataActivityStatus
from .industry_data_inbound_flow import IndustryDataInboundFlow
from .industry_data_inbound_api_flow import IndustryDataInboundApiFlow
from .industry_data_inbound_file_flow import IndustryDataInboundFileFlow

