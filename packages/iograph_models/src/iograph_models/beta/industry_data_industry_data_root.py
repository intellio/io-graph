from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from pydantic import BaseModel, Field


class IndustryDataIndustryDataRoot(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.industryData.industryDataRoot"] = Field(alias="@odata.type", default="#microsoft.graph.industryData.industryDataRoot")
	dataConnectors: Optional[list[Annotated[Union[IndustryDataOneRosterApiDataConnector, IndustryDataAzureDataLakeConnector],Field(discriminator="odata_type")]]] = Field(alias="dataConnectors", default=None,)
	inboundFlows: Optional[list[Annotated[Union[IndustryDataInboundApiFlow, IndustryDataInboundFileFlow],Field(discriminator="odata_type")]]] = Field(alias="inboundFlows", default=None,)
	operations: Optional[list[Annotated[Union[AttackSimulationOperation, EngagementAsyncOperation, GoalsExportJob, RichLongRunningOperation, IndustryDataFileValidateOperation],Field(discriminator="odata_type")]]] = Field(alias="operations", default=None,)
	outboundProvisioningFlowSets: Optional[list[IndustryDataOutboundProvisioningFlowSet]] = Field(alias="outboundProvisioningFlowSets", default=None,)
	referenceDefinitions: Optional[list[IndustryDataReferenceDefinition]] = Field(alias="referenceDefinitions", default=None,)
	roleGroups: Optional[list[IndustryDataRoleGroup]] = Field(alias="roleGroups", default=None,)
	runs: Optional[list[IndustryDataIndustryDataRun]] = Field(alias="runs", default=None,)
	sourceSystems: Optional[list[IndustryDataSourceSystemDefinition]] = Field(alias="sourceSystems", default=None,)
	years: Optional[list[IndustryDataYearTimePeriodDefinition]] = Field(alias="years", default=None,)

from .industry_data_one_roster_api_data_connector import IndustryDataOneRosterApiDataConnector
from .industry_data_azure_data_lake_connector import IndustryDataAzureDataLakeConnector
from .industry_data_inbound_api_flow import IndustryDataInboundApiFlow
from .industry_data_inbound_file_flow import IndustryDataInboundFileFlow
from .attack_simulation_operation import AttackSimulationOperation
from .engagement_async_operation import EngagementAsyncOperation
from .goals_export_job import GoalsExportJob
from .rich_long_running_operation import RichLongRunningOperation
from .industry_data_file_validate_operation import IndustryDataFileValidateOperation
from .industry_data_outbound_provisioning_flow_set import IndustryDataOutboundProvisioningFlowSet
from .industry_data_reference_definition import IndustryDataReferenceDefinition
from .industry_data_role_group import IndustryDataRoleGroup
from .industry_data_industry_data_run import IndustryDataIndustryDataRun
from .industry_data_source_system_definition import IndustryDataSourceSystemDefinition
from .industry_data_year_time_period_definition import IndustryDataYearTimePeriodDefinition
