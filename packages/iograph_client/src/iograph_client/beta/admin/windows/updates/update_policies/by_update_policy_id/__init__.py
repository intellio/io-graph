# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .compliance_changes import ComplianceChangesRequest
	from .audience import AudienceRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.beta.windows_updates_update_policy import WindowsUpdatesUpdatePolicy
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByUpdatePolicyIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/admin/windows/updates/updatePolicies/{updatePolicy%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> WindowsUpdatesUpdatePolicy:
		"""
		Get updatePolicy
		Read the properties and relationships of an updatePolicy object.
		Find more info here: https://learn.microsoft.com/graph/api/windowsupdates-updatepolicy-get?view=graph-rest-beta
		"""
		tags = ['admin.adminWindows']

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
		return await self.request_adapter.send_async(request_info, WindowsUpdatesUpdatePolicy, error_mapping)

	async def patch(
		self,
		body: WindowsUpdatesUpdatePolicy,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> WindowsUpdatesUpdatePolicy:
		"""
		Update updatePolicy
		Update the properties of an updatePolicy object.
		Find more info here: https://learn.microsoft.com/graph/api/windowsupdates-updatepolicy-update?view=graph-rest-beta
		"""
		tags = ['admin.adminWindows']

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
		return await self.request_adapter.send_async(request_info, WindowsUpdatesUpdatePolicy, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete updatePolicy
		Delete an updatePolicy object.
		Find more info here: https://learn.microsoft.com/graph/api/windowsupdates-updatepolicy-delete?view=graph-rest-beta
		"""
		tags = ['admin.adminWindows']
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



	def with_url(self, raw_url: str) -> ByUpdatePolicyIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByUpdatePolicyIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByUpdatePolicyIdRequest(self.request_adapter, self.path_parameters)

	def audience(self,
		updatePolicy_id: str,
	) -> AudienceRequest:
		if updatePolicy_id is None:
			raise TypeError("updatePolicy_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["updatePolicy%2Did"] =  updatePolicy_id

		from .audience import AudienceRequest
		return AudienceRequest(self.request_adapter, path_parameters)

	def compliance_changes(self,
		updatePolicy_id: str,
	) -> ComplianceChangesRequest:
		if updatePolicy_id is None:
			raise TypeError("updatePolicy_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["updatePolicy%2Did"] =  updatePolicy_id

		from .compliance_changes import ComplianceChangesRequest
		return ComplianceChangesRequest(self.request_adapter, path_parameters)

