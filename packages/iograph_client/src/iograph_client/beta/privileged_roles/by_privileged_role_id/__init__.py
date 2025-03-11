# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .summary import SummaryRequest
	from .settings import SettingsRequest
	from .self_deactivate import SelfDeactivateRequest
	from .self_activate import SelfActivateRequest
	from .assignments import AssignmentsRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.beta.privileged_role import PrivilegedRole
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByPrivilegedRoleIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/privilegedRoles/{privilegedRole%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> PrivilegedRole:
		"""
		Get entity from privilegedRoles by key
		
		"""
		tags = ['privilegedRoles.privilegedRole']

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
		return await self.request_adapter.send_async(request_info, PrivilegedRole, error_mapping)

	async def patch(
		self,
		body: PrivilegedRole,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> PrivilegedRole:
		"""
		Update entity in privilegedRoles
		
		"""
		tags = ['privilegedRoles.privilegedRole']

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
		return await self.request_adapter.send_async(request_info, PrivilegedRole, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete entity from privilegedRoles
		
		"""
		tags = ['privilegedRoles.privilegedRole']
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



	def with_url(self, raw_url: str) -> ByPrivilegedRoleIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByPrivilegedRoleIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByPrivilegedRoleIdRequest(self.request_adapter, self.path_parameters)

	def assignments(self,
		privilegedRole_id: str,
	) -> AssignmentsRequest:
		if privilegedRole_id is None:
			raise TypeError("privilegedRole_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["privilegedRole%2Did"] =  privilegedRole_id

		from .assignments import AssignmentsRequest
		return AssignmentsRequest(self.request_adapter, path_parameters)

	def self_activate(self,
		privilegedRole_id: str,
	) -> SelfActivateRequest:
		if privilegedRole_id is None:
			raise TypeError("privilegedRole_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["privilegedRole%2Did"] =  privilegedRole_id

		from .self_activate import SelfActivateRequest
		return SelfActivateRequest(self.request_adapter, path_parameters)

	def self_deactivate(self,
		privilegedRole_id: str,
	) -> SelfDeactivateRequest:
		if privilegedRole_id is None:
			raise TypeError("privilegedRole_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["privilegedRole%2Did"] =  privilegedRole_id

		from .self_deactivate import SelfDeactivateRequest
		return SelfDeactivateRequest(self.request_adapter, path_parameters)

	def settings(self,
		privilegedRole_id: str,
	) -> SettingsRequest:
		if privilegedRole_id is None:
			raise TypeError("privilegedRole_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["privilegedRole%2Did"] =  privilegedRole_id

		from .settings import SettingsRequest
		return SettingsRequest(self.request_adapter, path_parameters)

	def summary(self,
		privilegedRole_id: str,
	) -> SummaryRequest:
		if privilegedRole_id is None:
			raise TypeError("privilegedRole_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["privilegedRole%2Did"] =  privilegedRole_id

		from .summary import SummaryRequest
		return SummaryRequest(self.request_adapter, path_parameters)

