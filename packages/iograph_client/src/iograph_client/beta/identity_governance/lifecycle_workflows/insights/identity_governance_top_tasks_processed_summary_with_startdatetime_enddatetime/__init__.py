# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.identity_governance_top_tasks_processed_summary_with_startdatetime_enddatetime_get_response import Identity_governance_top_tasks_processed_summary_with_startdatetime_enddatetimeGetResponse


class IdentityGovernanceTopTasksProcessedSummaryWithStartDateTimeEndDateTimeRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identityGovernance/lifecycleWorkflows/insights/microsoft.graph.identityGovernance.topTasksProcessedSummary(startDateTime={startDateTime},endDateTime={endDateTime})", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Identity_governance_top_tasks_processed_summary_with_startdatetime_enddatetimeGetResponse:
		"""
		Invoke function topTasksProcessedSummary
		Provide a summary of the most processed tasks, known as top tasks, for a specified time period in a tenant. The task definition is provided, along with numerical counts of total, successful, and failed runs. For information about workflows processed, see insights: topWorkflowsProcessedSummary.
		Find more info here: https://learn.microsoft.com/graph/api/identitygovernance-insights-toptasksprocessedsummary?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, Identity_governance_top_tasks_processed_summary_with_startdatetime_enddatetimeGetResponse, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")

	def with_url(self, raw_url: str) -> IdentityGovernanceTopTasksProcessedSummaryWithStartDateTimeEndDateTimeRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: IdentityGovernanceTopTasksProcessedSummaryWithStartDateTimeEndDateTimeRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return IdentityGovernanceTopTasksProcessedSummaryWithStartDateTimeEndDateTimeRequest(self.request_adapter, self.path_parameters)

