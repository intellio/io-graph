from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class IndustryDataInboundFileFlow(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.industryData.inboundFileFlow"] = Field(alias="@odata.type", default="#microsoft.graph.industryData.inboundFileFlow")
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	readinessStatus: Optional[IndustryDataReadinessStatus | str] = Field(alias="readinessStatus", default=None,)
	dataDomain: Optional[IndustryDataInboundDomain | str] = Field(alias="dataDomain", default=None,)
	effectiveDateTime: Optional[datetime] = Field(alias="effectiveDateTime", default=None,)
	expirationDateTime: Optional[datetime] = Field(alias="expirationDateTime", default=None,)
	dataConnector: Optional[Union[IndustryDataApiDataConnector, IndustryDataOneRosterApiDataConnector, IndustryDataFileDataConnector, IndustryDataAzureDataLakeConnector]] = Field(alias="dataConnector", default=None,discriminator="odata_type", )
	year: Optional[IndustryDataYearTimePeriodDefinition] = Field(alias="year", default=None,)

from .industry_data_readiness_status import IndustryDataReadinessStatus
from .industry_data_inbound_domain import IndustryDataInboundDomain
from .industry_data_api_data_connector import IndustryDataApiDataConnector
from .industry_data_one_roster_api_data_connector import IndustryDataOneRosterApiDataConnector
from .industry_data_file_data_connector import IndustryDataFileDataConnector
from .industry_data_azure_data_lake_connector import IndustryDataAzureDataLakeConnector
from .industry_data_year_time_period_definition import IndustryDataYearTimePeriodDefinition

