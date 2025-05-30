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
	from .has_payload_links import HasPayloadLinksRequest
	from .create_enrollment_notification_configuration import CreateEnrollmentNotificationConfigurationRequest
	from .count import CountRequest
	from .by_device_enrollment_configuration_id import ByDeviceEnrollmentConfigurationIdRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.device_enrollment_configuration import DeviceEnrollmentConfiguration
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.device_enrollment_configuration_collection_response import DeviceEnrollmentConfigurationCollectionResponse


class DeviceEnrollmentConfigurationsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/deviceEnrollmentConfigurations", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DeviceEnrollmentConfigurationCollectionResponse:
		"""
		Get deviceEnrollmentConfigurations from users
		Get enrollment configurations targeted to the user
		"""
		tags = ['users.deviceEnrollmentConfiguration']

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
		return await self.request_adapter.send_async(request_info, DeviceEnrollmentConfigurationCollectionResponse, error_mapping)

	async def post(
		self,
		body: DeviceEnrollmentConfiguration,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> DeviceEnrollmentConfiguration:
		"""
		Create new navigation property to deviceEnrollmentConfigurations for users
		
		"""
		tags = ['users.deviceEnrollmentConfiguration']

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
		return await self.request_adapter.send_async(request_info, DeviceEnrollmentConfiguration, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> DeviceEnrollmentConfigurationsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: DeviceEnrollmentConfigurationsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return DeviceEnrollmentConfigurationsRequest(self.request_adapter, self.path_parameters)

	def by_device_enrollment_configuration_id(self,
		user_id: str,
		deviceEnrollmentConfiguration_id: str,
	) -> ByDeviceEnrollmentConfigurationIdRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if deviceEnrollmentConfiguration_id is None:
			raise TypeError("deviceEnrollmentConfiguration_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["deviceEnrollmentConfiguration%2Did"] =  deviceEnrollmentConfiguration_id

		from .by_device_enrollment_configuration_id import ByDeviceEnrollmentConfigurationIdRequest
		return ByDeviceEnrollmentConfigurationIdRequest(self.request_adapter, path_parameters)

	def count(self,
		user_id: str,
	) -> CountRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

	def create_enrollment_notification_configuration(self,
		user_id: str,
	) -> CreateEnrollmentNotificationConfigurationRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .create_enrollment_notification_configuration import CreateEnrollmentNotificationConfigurationRequest
		return CreateEnrollmentNotificationConfigurationRequest(self.request_adapter, path_parameters)

	def has_payload_links(self,
		user_id: str,
	) -> HasPayloadLinksRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .has_payload_links import HasPayloadLinksRequest
		return HasPayloadLinksRequest(self.request_adapter, path_parameters)

