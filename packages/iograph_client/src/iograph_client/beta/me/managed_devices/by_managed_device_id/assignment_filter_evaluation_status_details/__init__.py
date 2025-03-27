# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_assignment_filter_evaluation_status_details_id import ByAssignmentFilterEvaluationStatusDetailsIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.assignment_filter_evaluation_status_details import AssignmentFilterEvaluationStatusDetails
from iograph_models.beta.assignment_filter_evaluation_status_details_collection_response import AssignmentFilterEvaluationStatusDetailsCollectionResponse


class AssignmentFilterEvaluationStatusDetailsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/me/managedDevices/{managedDevice%2Did}/assignmentFilterEvaluationStatusDetails", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AssignmentFilterEvaluationStatusDetailsCollectionResponse:
		"""
		Get assignmentFilterEvaluationStatusDetails from me
		Managed device mobile app configuration states for this device.
		"""
		tags = ['me.managedDevice']

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
		return await self.request_adapter.send_async(request_info, AssignmentFilterEvaluationStatusDetailsCollectionResponse, error_mapping)

	async def post(
		self,
		body: AssignmentFilterEvaluationStatusDetails,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> AssignmentFilterEvaluationStatusDetails:
		"""
		Create new navigation property to assignmentFilterEvaluationStatusDetails for me
		
		"""
		tags = ['me.managedDevice']

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.POST,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		request_info.set_content(body, "application/json")
		return await self.request_adapter.send_async(request_info, AssignmentFilterEvaluationStatusDetails, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> AssignmentFilterEvaluationStatusDetailsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: AssignmentFilterEvaluationStatusDetailsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return AssignmentFilterEvaluationStatusDetailsRequest(self.request_adapter, self.path_parameters)

	def by_assignment_filter_evaluation_status_details_id(self,
		managedDevice_id: str,
		assignmentFilterEvaluationStatusDetails_id: str,
	) -> ByAssignmentFilterEvaluationStatusDetailsIdRequest:
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")
		if assignmentFilterEvaluationStatusDetails_id is None:
			raise TypeError("assignmentFilterEvaluationStatusDetails_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedDevice%2Did"] =  managedDevice_id
		path_parameters["assignmentFilterEvaluationStatusDetails%2Did"] =  assignmentFilterEvaluationStatusDetails_id

		from .by_assignment_filter_evaluation_status_details_id import ByAssignmentFilterEvaluationStatusDetailsIdRequest
		return ByAssignmentFilterEvaluationStatusDetailsIdRequest(self.request_adapter, path_parameters)

	def count(self,
		managedDevice_id: str,
	) -> CountRequest:
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

