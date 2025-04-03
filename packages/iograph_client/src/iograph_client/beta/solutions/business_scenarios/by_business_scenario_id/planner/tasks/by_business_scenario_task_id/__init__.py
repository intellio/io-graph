# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .progress_task_board_format import ProgressTaskBoardFormatRequest
	from .details import DetailsRequest
	from .bucket_task_board_format import BucketTaskBoardFormatRequest
	from .assigned_to_task_board_format import AssignedToTaskBoardFormatRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.business_scenario_task import BusinessScenarioTask


class ByBusinessScenarioTaskIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/solutions/businessScenarios/{businessScenario%2Did}/planner/tasks/{businessScenarioTask%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> BusinessScenarioTask:
		"""
		Get businessScenarioTask
		Read the properties and relationships of a businessScenarioTask object.
		Find more info here: https://learn.microsoft.com/graph/api/businessscenariotask-get?view=graph-rest-beta
		"""
		tags = ['solutions.businessScenario']

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
		return await self.request_adapter.send_async(request_info, BusinessScenarioTask, error_mapping)

	async def patch(
		self,
		body: BusinessScenarioTask,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> BusinessScenarioTask:
		"""
		Update businessScenarioTask
		Update the properties of a businessScenarioTask object.
		Find more info here: https://learn.microsoft.com/graph/api/businessscenariotask-update?view=graph-rest-beta
		"""
		tags = ['solutions.businessScenario']

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
		return await self.request_adapter.send_async(request_info, BusinessScenarioTask, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete businessScenarioTask
		Delete a businessScenarioTask object.
		Find more info here: https://learn.microsoft.com/graph/api/businessscenarioplanner-delete-tasks?view=graph-rest-beta
		"""
		tags = ['solutions.businessScenario']
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



	def with_url(self, raw_url: str) -> ByBusinessScenarioTaskIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByBusinessScenarioTaskIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByBusinessScenarioTaskIdRequest(self.request_adapter, self.path_parameters)

	def assigned_to_task_board_format(self,
		businessScenario_id: str,
		businessScenarioTask_id: str,
	) -> AssignedToTaskBoardFormatRequest:
		if businessScenario_id is None:
			raise TypeError("businessScenario_id cannot be null.")
		if businessScenarioTask_id is None:
			raise TypeError("businessScenarioTask_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["businessScenario%2Did"] =  businessScenario_id
		path_parameters["businessScenarioTask%2Did"] =  businessScenarioTask_id

		from .assigned_to_task_board_format import AssignedToTaskBoardFormatRequest
		return AssignedToTaskBoardFormatRequest(self.request_adapter, path_parameters)

	def bucket_task_board_format(self,
		businessScenario_id: str,
		businessScenarioTask_id: str,
	) -> BucketTaskBoardFormatRequest:
		if businessScenario_id is None:
			raise TypeError("businessScenario_id cannot be null.")
		if businessScenarioTask_id is None:
			raise TypeError("businessScenarioTask_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["businessScenario%2Did"] =  businessScenario_id
		path_parameters["businessScenarioTask%2Did"] =  businessScenarioTask_id

		from .bucket_task_board_format import BucketTaskBoardFormatRequest
		return BucketTaskBoardFormatRequest(self.request_adapter, path_parameters)

	def details(self,
		businessScenario_id: str,
		businessScenarioTask_id: str,
	) -> DetailsRequest:
		if businessScenario_id is None:
			raise TypeError("businessScenario_id cannot be null.")
		if businessScenarioTask_id is None:
			raise TypeError("businessScenarioTask_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["businessScenario%2Did"] =  businessScenario_id
		path_parameters["businessScenarioTask%2Did"] =  businessScenarioTask_id

		from .details import DetailsRequest
		return DetailsRequest(self.request_adapter, path_parameters)

	def progress_task_board_format(self,
		businessScenario_id: str,
		businessScenarioTask_id: str,
	) -> ProgressTaskBoardFormatRequest:
		if businessScenario_id is None:
			raise TypeError("businessScenario_id cannot be null.")
		if businessScenarioTask_id is None:
			raise TypeError("businessScenarioTask_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["businessScenario%2Did"] =  businessScenario_id
		path_parameters["businessScenarioTask%2Did"] =  businessScenarioTask_id

		from .progress_task_board_format import ProgressTaskBoardFormatRequest
		return ProgressTaskBoardFormatRequest(self.request_adapter, path_parameters)

