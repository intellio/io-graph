# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .........request_adapter import HttpxRequestAdapter
from iograph_models.beta.managed_tenants_change_deployment_status_post_request import Managed_tenants_change_deployment_statusPostRequest
from iograph_models.beta.managed_tenants_management_template_step_deployment import ManagedTenantsManagementTemplateStepDeployment
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ManagedTenantsChangeDeploymentStatusRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/tenantRelationships/managedTenants/managementTemplateStepVersions/{managementTemplateStepVersion%2Did}/deployments/{managementTemplateStepDeployment%2Did}/microsoft.graph.managedTenants.changeDeploymentStatus", path_parameters)

	async def post(
		self,
		body: Managed_tenants_change_deployment_statusPostRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ManagedTenantsManagementTemplateStepDeployment:
		"""
		Invoke action changeDeploymentStatus
		
		"""
		tags = ['tenantRelationships.managedTenant']

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
		return await self.request_adapter.send_async(request_info, ManagedTenantsManagementTemplateStepDeployment, error_mapping)


	def with_url(self, raw_url: str) -> ManagedTenantsChangeDeploymentStatusRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ManagedTenantsChangeDeploymentStatusRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ManagedTenantsChangeDeploymentStatusRequest(self.request_adapter, self.path_parameters)

