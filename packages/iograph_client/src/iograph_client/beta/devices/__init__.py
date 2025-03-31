# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ...request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .validate_properties import ValidatePropertiesRequest
	from .get_user_owned_objects import GetUserOwnedObjectsRequest
	from .get_by_ids import GetByIdsRequest
	from .delta import DeltaRequest
	from .count import CountRequest
	from .by_device_id import ByDeviceIdRequest
	from ...request_adapter import HttpxRequestAdapter
from iograph_models.beta.device_collection_response import DeviceCollectionResponse
from iograph_models.beta.device import Device
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class DevicesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/devices", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DeviceCollectionResponse:
		"""
		List devices
		Retrieve a list of devices registered in the directory.
		Find more info here: https://learn.microsoft.com/graph/api/device-list?view=graph-rest-beta
		"""
		tags = ['devices.device']
		header_parameters = [{'name': 'ConsistencyLevel', 'in': 'header', 'description': 'Indicates the requested consistency level. Documentation URL: https://docs.microsoft.com/graph/aad-advanced-queries', 'schema': {'type': 'string'}, 'examples': {'example-1': {'description': "$search and $count queries require the client to set the ConsistencyLevel HTTP header to 'eventual'.", 'value': 'eventual'}}}]

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
		return await self.request_adapter.send_async(request_info, DeviceCollectionResponse, error_mapping)

	async def post(
		self,
		body: Device,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Device:
		"""
		Create device
		Create a new device.
		Find more info here: https://learn.microsoft.com/graph/api/device-post-devices?view=graph-rest-beta
		"""
		tags = ['devices.device']

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
		return await self.request_adapter.send_async(request_info, Device, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> DevicesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: DevicesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return DevicesRequest(self.request_adapter, self.path_parameters)

	def by_device_id(self,
		device_id: str,
	) -> ByDeviceIdRequest:
		if device_id is None:
			raise TypeError("device_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["device%2Did"] =  device_id

		from .by_device_id import ByDeviceIdRequest
		return ByDeviceIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

	@property
	def delta(self,
	) -> DeltaRequest:
		from .delta import DeltaRequest
		return DeltaRequest(self.request_adapter, self.path_parameters)

	@property
	def get_by_ids(self,
	) -> GetByIdsRequest:
		from .get_by_ids import GetByIdsRequest
		return GetByIdsRequest(self.request_adapter, self.path_parameters)

	@property
	def get_user_owned_objects(self,
	) -> GetUserOwnedObjectsRequest:
		from .get_user_owned_objects import GetUserOwnedObjectsRequest
		return GetUserOwnedObjectsRequest(self.request_adapter, self.path_parameters)

	@property
	def validate_properties(self,
	) -> ValidatePropertiesRequest:
		from .validate_properties import ValidatePropertiesRequest
		return ValidatePropertiesRequest(self.request_adapter, self.path_parameters)

