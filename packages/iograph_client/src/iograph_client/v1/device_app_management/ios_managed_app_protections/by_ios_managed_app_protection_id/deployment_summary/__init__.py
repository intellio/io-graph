# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.v1.managed_app_policy_deployment_summary import ManagedAppPolicyDeploymentSummary
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class DeploymentSummaryRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceAppManagement/iosManagedAppProtections/{iosManagedAppProtection%2Did}/deploymentSummary", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ManagedAppPolicyDeploymentSummary:
		"""
		Get managedAppPolicyDeploymentSummary
		Read properties and relationships of the managedAppPolicyDeploymentSummary object.
		Find more info here: https://learn.microsoft.com/graph/api/intune-mam-managedapppolicydeploymentsummary-get?view=graph-rest-1.0
		"""
		tags = ['deviceAppManagement.iosManagedAppProtection']

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
		return await self.request_adapter.send_async(request_info, ManagedAppPolicyDeploymentSummary, error_mapping)

	async def patch(
		self,
		body: ManagedAppPolicyDeploymentSummary,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ManagedAppPolicyDeploymentSummary:
		"""
		Update managedAppPolicyDeploymentSummary
		Update the properties of a managedAppPolicyDeploymentSummary object.
		Find more info here: https://learn.microsoft.com/graph/api/intune-mam-managedapppolicydeploymentsummary-update?view=graph-rest-1.0
		"""
		tags = ['deviceAppManagement.iosManagedAppProtection']

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
		return await self.request_adapter.send_async(request_info, ManagedAppPolicyDeploymentSummary, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property deploymentSummary for deviceAppManagement
		
		"""
		tags = ['deviceAppManagement.iosManagedAppProtection']
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



	def with_url(self, raw_url: str) -> DeploymentSummaryRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: DeploymentSummaryRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return DeploymentSummaryRequest(self.request_adapter, self.path_parameters)

