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
	from .usage_rights import UsageRightsRequest
	from .transitive_member_of import TransitiveMemberOfRequest
	from .registered_users import RegisteredUsersRequest
	from .registered_owners import RegisteredOwnersRequest
	from .member_of import MemberOfRequest
	from .extensions import ExtensionsRequest
	from .device_template import DeviceTemplateRequest
	from .commands import CommandsRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.device import Device
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByDeviceIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/devices/{device%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Device:
		"""
		Get devices from users
		
		"""
		tags = ['users.device']

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
		return await self.request_adapter.send_async(request_info, Device, error_mapping)

	async def patch(
		self,
		body: Device,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Device:
		"""
		Update the navigation property devices in users
		
		"""
		tags = ['users.device']

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
		return await self.request_adapter.send_async(request_info, Device, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property devices for users
		
		"""
		tags = ['users.device']
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



	def with_url(self, raw_url: str) -> ByDeviceIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByDeviceIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByDeviceIdRequest(self.request_adapter, self.path_parameters)

	def commands(self,
		user_id: str,
		device_id: str,
	) -> CommandsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if device_id is None:
			raise TypeError("device_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["device%2Did"] =  device_id

		from .commands import CommandsRequest
		return CommandsRequest(self.request_adapter, path_parameters)

	def device_template(self,
		user_id: str,
		device_id: str,
	) -> DeviceTemplateRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if device_id is None:
			raise TypeError("device_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["device%2Did"] =  device_id

		from .device_template import DeviceTemplateRequest
		return DeviceTemplateRequest(self.request_adapter, path_parameters)

	def extensions(self,
		user_id: str,
		device_id: str,
	) -> ExtensionsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if device_id is None:
			raise TypeError("device_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["device%2Did"] =  device_id

		from .extensions import ExtensionsRequest
		return ExtensionsRequest(self.request_adapter, path_parameters)

	def member_of(self,
		user_id: str,
		device_id: str,
	) -> MemberOfRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if device_id is None:
			raise TypeError("device_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["device%2Did"] =  device_id

		from .member_of import MemberOfRequest
		return MemberOfRequest(self.request_adapter, path_parameters)

	def registered_owners(self,
		user_id: str,
		device_id: str,
	) -> RegisteredOwnersRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if device_id is None:
			raise TypeError("device_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["device%2Did"] =  device_id

		from .registered_owners import RegisteredOwnersRequest
		return RegisteredOwnersRequest(self.request_adapter, path_parameters)

	def registered_users(self,
		user_id: str,
		device_id: str,
	) -> RegisteredUsersRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if device_id is None:
			raise TypeError("device_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["device%2Did"] =  device_id

		from .registered_users import RegisteredUsersRequest
		return RegisteredUsersRequest(self.request_adapter, path_parameters)

	def transitive_member_of(self,
		user_id: str,
		device_id: str,
	) -> TransitiveMemberOfRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if device_id is None:
			raise TypeError("device_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["device%2Did"] =  device_id

		from .transitive_member_of import TransitiveMemberOfRequest
		return TransitiveMemberOfRequest(self.request_adapter, path_parameters)

	def usage_rights(self,
		user_id: str,
		device_id: str,
	) -> UsageRightsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if device_id is None:
			raise TypeError("device_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["device%2Did"] =  device_id

		from .usage_rights import UsageRightsRequest
		return UsageRightsRequest(self.request_adapter, path_parameters)

