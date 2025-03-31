# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .identity_governance_workflows_processed_summary_with_startdatetime_enddatetime import IdentityGovernanceWorkflowsProcessedSummaryWithStartDateTimeEndDateTimeRequest
	from .identity_governance_workflows_processed_by_category_with_startdatetime_enddatetime import IdentityGovernanceWorkflowsProcessedByCategoryWithStartDateTimeEndDateTimeRequest
	from .identity_governance_top_workflows_processed_summary_with_startdatetime_enddatetime import IdentityGovernanceTopWorkflowsProcessedSummaryWithStartDateTimeEndDateTimeRequest
	from .identity_governance_top_tasks_processed_summary_with_startdatetime_enddatetime import IdentityGovernanceTopTasksProcessedSummaryWithStartDateTimeEndDateTimeRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.v1.identity_governance_insights import IdentityGovernanceInsights
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class InsightsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identityGovernance/lifecycleWorkflows/insights", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> IdentityGovernanceInsights:
		"""
		Get insights from identityGovernance
		The insight container holding workflow insight summaries for a tenant.
		"""
		tags = ['identityGovernance.lifecycleWorkflowsContainer']

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.GET,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		return await self.request_adapter.send_async(request_info, IdentityGovernanceInsights, error_mapping)

	async def patch(
		self,
		body: IdentityGovernanceInsights,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> IdentityGovernanceInsights:
		"""
		Update the navigation property insights in identityGovernance
		
		"""
		tags = ['identityGovernance.lifecycleWorkflowsContainer']

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.PATCH,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		request_info.set_content(body, "application/json")
		return await self.request_adapter.send_async(request_info, IdentityGovernanceInsights, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property insights for identityGovernance
		
		"""
		tags = ['identityGovernance.lifecycleWorkflowsContainer']
		header_parameters = [{'name': 'If-Match', 'in': 'header', 'description': 'ETag', 'schema': {'type': 'string'}}]

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.DELETE,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")



	def with_url(self, raw_url: str) -> InsightsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: InsightsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return InsightsRequest(self.request_adapter, self.path_parameters)

	def identity_governance_top_tasks_processed_summary_with_startdatetime_enddatetime(self,
		startDateTime: datetime,
		endDateTime: datetime,
	) -> IdentityGovernanceTopTasksProcessedSummaryWithStartDateTimeEndDateTimeRequest:
		if startDateTime is None:
			raise TypeError("startDateTime cannot be null.")
		if endDateTime is None:
			raise TypeError("endDateTime cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["startDateTime"] =  startDateTime
		path_parameters["endDateTime"] =  endDateTime

		from .identity_governance_top_tasks_processed_summary_with_startdatetime_enddatetime import IdentityGovernanceTopTasksProcessedSummaryWithStartDateTimeEndDateTimeRequest
		return IdentityGovernanceTopTasksProcessedSummaryWithStartDateTimeEndDateTimeRequest(self.request_adapter, path_parameters)

	def identity_governance_top_workflows_processed_summary_with_startdatetime_enddatetime(self,
		startDateTime: datetime,
		endDateTime: datetime,
	) -> IdentityGovernanceTopWorkflowsProcessedSummaryWithStartDateTimeEndDateTimeRequest:
		if startDateTime is None:
			raise TypeError("startDateTime cannot be null.")
		if endDateTime is None:
			raise TypeError("endDateTime cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["startDateTime"] =  startDateTime
		path_parameters["endDateTime"] =  endDateTime

		from .identity_governance_top_workflows_processed_summary_with_startdatetime_enddatetime import IdentityGovernanceTopWorkflowsProcessedSummaryWithStartDateTimeEndDateTimeRequest
		return IdentityGovernanceTopWorkflowsProcessedSummaryWithStartDateTimeEndDateTimeRequest(self.request_adapter, path_parameters)

	def identity_governance_workflows_processed_by_category_with_startdatetime_enddatetime(self,
		startDateTime: datetime,
		endDateTime: datetime,
	) -> IdentityGovernanceWorkflowsProcessedByCategoryWithStartDateTimeEndDateTimeRequest:
		if startDateTime is None:
			raise TypeError("startDateTime cannot be null.")
		if endDateTime is None:
			raise TypeError("endDateTime cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["startDateTime"] =  startDateTime
		path_parameters["endDateTime"] =  endDateTime

		from .identity_governance_workflows_processed_by_category_with_startdatetime_enddatetime import IdentityGovernanceWorkflowsProcessedByCategoryWithStartDateTimeEndDateTimeRequest
		return IdentityGovernanceWorkflowsProcessedByCategoryWithStartDateTimeEndDateTimeRequest(self.request_adapter, path_parameters)

	def identity_governance_workflows_processed_summary_with_startdatetime_enddatetime(self,
		startDateTime: datetime,
		endDateTime: datetime,
	) -> IdentityGovernanceWorkflowsProcessedSummaryWithStartDateTimeEndDateTimeRequest:
		if startDateTime is None:
			raise TypeError("startDateTime cannot be null.")
		if endDateTime is None:
			raise TypeError("endDateTime cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["startDateTime"] =  startDateTime
		path_parameters["endDateTime"] =  endDateTime

		from .identity_governance_workflows_processed_summary_with_startdatetime_enddatetime import IdentityGovernanceWorkflowsProcessedSummaryWithStartDateTimeEndDateTimeRequest
		return IdentityGovernanceWorkflowsProcessedSummaryWithStartDateTimeEndDateTimeRequest(self.request_adapter, path_parameters)

