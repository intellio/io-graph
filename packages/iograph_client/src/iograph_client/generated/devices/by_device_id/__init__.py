# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .transitive_member_of import TransitiveMemberOfRequest
	from .registered_users import RegisteredUsersRequest
	from .registered_owners import RegisteredOwnersRequest
	from .restore import RestoreRequest
	from .get_member_objects import GetMemberObjectsRequest
	from .get_member_groups import GetMemberGroupsRequest
	from .check_member_objects import CheckMemberObjectsRequest
	from .check_member_groups import CheckMemberGroupsRequest
	from .member_of import MemberOfRequest
	from .extensions import ExtensionsRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.device import Device


class ByDeviceIdRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/devices/{device%2Did}"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Device:
		"""
		Get device
		Get the properties and relationships of a device object.
		Find more info here: https://learn.microsoft.com/graph/api/device-get?view=graph-rest-1.0
		"""
		tags = ['devices.device']

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
		Update device
		Update the properties of a registered device. Only certain properties of a device can be updated through approved Mobile Device Managment (MDM) apps.
		Find more info here: https://learn.microsoft.com/graph/api/device-update?view=graph-rest-1.0
		"""
		tags = ['devices.device']

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
		Delete device
		Delete a registered device.
		Find more info here: https://learn.microsoft.com/graph/api/device-delete?view=graph-rest-1.0
		"""
		tags = ['devices.device']
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



	@property
	def extensions(self,
	) -> ExtensionsRequest:
		from .extensions import ExtensionsRequest
		return ExtensionsRequest(self.request_adapter, self.path_parameters)

	@property
	def member_of(self,
	) -> MemberOfRequest:
		from .member_of import MemberOfRequest
		return MemberOfRequest(self.request_adapter, self.path_parameters)

	@property
	def check_member_groups(self,
	) -> CheckMemberGroupsRequest:
		from .check_member_groups import CheckMemberGroupsRequest
		return CheckMemberGroupsRequest(self.request_adapter, self.path_parameters)

	@property
	def check_member_objects(self,
	) -> CheckMemberObjectsRequest:
		from .check_member_objects import CheckMemberObjectsRequest
		return CheckMemberObjectsRequest(self.request_adapter, self.path_parameters)

	@property
	def get_member_groups(self,
	) -> GetMemberGroupsRequest:
		from .get_member_groups import GetMemberGroupsRequest
		return GetMemberGroupsRequest(self.request_adapter, self.path_parameters)

	@property
	def get_member_objects(self,
	) -> GetMemberObjectsRequest:
		from .get_member_objects import GetMemberObjectsRequest
		return GetMemberObjectsRequest(self.request_adapter, self.path_parameters)

	@property
	def restore(self,
	) -> RestoreRequest:
		from .restore import RestoreRequest
		return RestoreRequest(self.request_adapter, self.path_parameters)

	@property
	def registered_owners(self,
	) -> RegisteredOwnersRequest:
		from .registered_owners import RegisteredOwnersRequest
		return RegisteredOwnersRequest(self.request_adapter, self.path_parameters)

	@property
	def registered_users(self,
	) -> RegisteredUsersRequest:
		from .registered_users import RegisteredUsersRequest
		return RegisteredUsersRequest(self.request_adapter, self.path_parameters)

	@property
	def transitive_member_of(self,
	) -> TransitiveMemberOfRequest:
		from .transitive_member_of import TransitiveMemberOfRequest
		return TransitiveMemberOfRequest(self.request_adapter, self.path_parameters)

