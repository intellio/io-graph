from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class IndustryDataInboundApiFlow(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	readinessStatus: Optional[IndustryDataReadinessStatus | str] = Field(alias="readinessStatus",default=None,)
	dataDomain: Optional[IndustryDataInboundDomain | str] = Field(alias="dataDomain",default=None,)
	effectiveDateTime: Optional[datetime] = Field(alias="effectiveDateTime",default=None,)
	expirationDateTime: Optional[datetime] = Field(alias="expirationDateTime",default=None,)
	dataConnector: SerializeAsAny[Optional[IndustryDataIndustryDataConnector]] = Field(alias="dataConnector",default=None,)
	year: Optional[IndustryDataYearTimePeriodDefinition] = Field(alias="year",default=None,)

from .industry_data_readiness_status import IndustryDataReadinessStatus
from .industry_data_inbound_domain import IndustryDataInboundDomain
from .industry_data_industry_data_connector import IndustryDataIndustryDataConnector
from .industry_data_year_time_period_definition import IndustryDataYearTimePeriodDefinition

