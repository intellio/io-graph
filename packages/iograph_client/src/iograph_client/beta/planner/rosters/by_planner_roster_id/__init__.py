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
	from .plans import PlansRequest
	from .assign_sensitivity_label import AssignSensitivityLabelRequest
	from .members import MembersRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.planner_roster import PlannerRoster


class ByPlannerRosterIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/planner/rosters/{plannerRoster%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> PlannerRoster:
		"""
		Get plannerRoster
		Read the properties and relationships of a plannerRoster object.
		Find more info here: https://learn.microsoft.com/graph/api/plannerroster-get?view=graph-rest-beta
		"""
		tags = ['planner.plannerRoster']

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
		return await self.request_adapter.send_async(request_info, PlannerRoster, error_mapping)

	async def patch(
		self,
		body: PlannerRoster,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> PlannerRoster:
		"""
		Update the navigation property rosters in planner
		
		"""
		tags = ['planner.plannerRoster']

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
		return await self.request_adapter.send_async(request_info, PlannerRoster, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete plannerRoster
		Delete a plannerRoster object.
		Find more info here: https://learn.microsoft.com/graph/api/plannerroster-delete?view=graph-rest-beta
		"""
		tags = ['planner.plannerRoster']
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



	def with_url(self, raw_url: str) -> ByPlannerRosterIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByPlannerRosterIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByPlannerRosterIdRequest(self.request_adapter, self.path_parameters)

	def members(self,
		plannerRoster_id: str,
	) -> MembersRequest:
		if plannerRoster_id is None:
			raise TypeError("plannerRoster_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["plannerRoster%2Did"] =  plannerRoster_id

		from .members import MembersRequest
		return MembersRequest(self.request_adapter, path_parameters)

	def assign_sensitivity_label(self,
		plannerRoster_id: str,
	) -> AssignSensitivityLabelRequest:
		if plannerRoster_id is None:
			raise TypeError("plannerRoster_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["plannerRoster%2Did"] =  plannerRoster_id

		from .assign_sensitivity_label import AssignSensitivityLabelRequest
		return AssignSensitivityLabelRequest(self.request_adapter, path_parameters)

	def plans(self,
		plannerRoster_id: str,
	) -> PlansRequest:
		if plannerRoster_id is None:
			raise TypeError("plannerRoster_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["plannerRoster%2Did"] =  plannerRoster_id

		from .plans import PlansRequest
		return PlansRequest(self.request_adapter, path_parameters)

