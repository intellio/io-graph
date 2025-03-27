# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .scheduled_permissions_requests import ScheduledPermissionsRequestsRequest
	from .scheduled_permissions_approvals import ScheduledPermissionsApprovalsRequest
	from .permissions_request_changes import PermissionsRequestChangesRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.permissions_management import PermissionsManagement


class PermissionsManagementRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identityGovernance/permissionsManagement", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> PermissionsManagement:
		"""
		Get permissionsManagement from identityGovernance
		
		"""
		tags = ['identityGovernance.permissionsManagement']

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
		return await self.request_adapter.send_async(request_info, PermissionsManagement, error_mapping)

	async def patch(
		self,
		body: PermissionsManagement,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> PermissionsManagement:
		"""
		Update the navigation property permissionsManagement in identityGovernance
		
		"""
		tags = ['identityGovernance.permissionsManagement']

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
		return await self.request_adapter.send_async(request_info, PermissionsManagement, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property permissionsManagement for identityGovernance
		
		"""
		tags = ['identityGovernance.permissionsManagement']
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



	def with_url(self, raw_url: str) -> PermissionsManagementRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: PermissionsManagementRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return PermissionsManagementRequest(self.request_adapter, self.path_parameters)

	@property
	def permissions_request_changes(self,
	) -> PermissionsRequestChangesRequest:
		from .permissions_request_changes import PermissionsRequestChangesRequest
		return PermissionsRequestChangesRequest(self.request_adapter, self.path_parameters)

	@property
	def scheduled_permissions_approvals(self,
	) -> ScheduledPermissionsApprovalsRequest:
		from .scheduled_permissions_approvals import ScheduledPermissionsApprovalsRequest
		return ScheduledPermissionsApprovalsRequest(self.request_adapter, self.path_parameters)

	@property
	def scheduled_permissions_requests(self,
	) -> ScheduledPermissionsRequestsRequest:
		from .scheduled_permissions_requests import ScheduledPermissionsRequestsRequest
		return ScheduledPermissionsRequestsRequest(self.request_adapter, self.path_parameters)

