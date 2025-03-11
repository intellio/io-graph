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
	from .by_hardware_configuration_assignment_id import ByHardwareConfigurationAssignmentIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.hardware_configuration_assignment_collection_response import HardwareConfigurationAssignmentCollectionResponse
from iograph_models.beta.hardware_configuration_assignment import HardwareConfigurationAssignment
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class AssignmentsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/hardwareConfigurations/{hardwareConfiguration%2Did}/assignments", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> HardwareConfigurationAssignmentCollectionResponse:
		"""
		Get assignments from deviceManagement
		A list of the Entra user group ids that hardware configuration will be applied to. Only security groups and Office 365 Groups are supported. Optional.
		"""
		tags = ['deviceManagement.hardwareConfiguration']

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
		return await self.request_adapter.send_async(request_info, HardwareConfigurationAssignmentCollectionResponse, error_mapping)

	async def post(
		self,
		body: HardwareConfigurationAssignment,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> HardwareConfigurationAssignment:
		"""
		Create new navigation property to assignments for deviceManagement
		
		"""
		tags = ['deviceManagement.hardwareConfiguration']

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
		return await self.request_adapter.send_async(request_info, HardwareConfigurationAssignment, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> AssignmentsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: AssignmentsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return AssignmentsRequest(self.request_adapter, self.path_parameters)

	def by_hardware_configuration_assignment_id(self,
		hardwareConfiguration_id: str,
		hardwareConfigurationAssignment_id: str,
	) -> ByHardwareConfigurationAssignmentIdRequest:
		if hardwareConfiguration_id is None:
			raise TypeError("hardwareConfiguration_id cannot be null.")
		if hardwareConfigurationAssignment_id is None:
			raise TypeError("hardwareConfigurationAssignment_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["hardwareConfiguration%2Did"] =  hardwareConfiguration_id
		path_parameters["hardwareConfigurationAssignment%2Did"] =  hardwareConfigurationAssignment_id

		from .by_hardware_configuration_assignment_id import ByHardwareConfigurationAssignmentIdRequest
		return ByHardwareConfigurationAssignmentIdRequest(self.request_adapter, path_parameters)

	def count(self,
		hardwareConfiguration_id: str,
	) -> CountRequest:
		if hardwareConfiguration_id is None:
			raise TypeError("hardwareConfiguration_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["hardwareConfiguration%2Did"] =  hardwareConfiguration_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

