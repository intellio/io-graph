from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IndustryDataIndustryDataRoot(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	dataConnectors: SerializeAsAny[Optional[list[IndustryDataIndustryDataConnector]]] = Field(alias="dataConnectors",default=None,)
	inboundFlows: SerializeAsAny[Optional[list[IndustryDataInboundFlow]]] = Field(alias="inboundFlows",default=None,)
	operations: SerializeAsAny[Optional[list[LongRunningOperation]]] = Field(alias="operations",default=None,)
	outboundProvisioningFlowSets: Optional[list[IndustryDataOutboundProvisioningFlowSet]] = Field(alias="outboundProvisioningFlowSets",default=None,)
	referenceDefinitions: Optional[list[IndustryDataReferenceDefinition]] = Field(alias="referenceDefinitions",default=None,)
	roleGroups: Optional[list[IndustryDataRoleGroup]] = Field(alias="roleGroups",default=None,)
	runs: Optional[list[IndustryDataIndustryDataRun]] = Field(alias="runs",default=None,)
	sourceSystems: Optional[list[IndustryDataSourceSystemDefinition]] = Field(alias="sourceSystems",default=None,)
	years: Optional[list[IndustryDataYearTimePeriodDefinition]] = Field(alias="years",default=None,)

from .industry_data_industry_data_connector import IndustryDataIndustryDataConnector
from .industry_data_inbound_flow import IndustryDataInboundFlow
from .long_running_operation import LongRunningOperation
from .industry_data_outbound_provisioning_flow_set import IndustryDataOutboundProvisioningFlowSet
from .industry_data_reference_definition import IndustryDataReferenceDefinition
from .industry_data_role_group import IndustryDataRoleGroup
from .industry_data_industry_data_run import IndustryDataIndustryDataRun
from .industry_data_source_system_definition import IndustryDataSourceSystemDefinition
from .industry_data_year_time_period_definition import IndustryDataYearTimePeriodDefinition

