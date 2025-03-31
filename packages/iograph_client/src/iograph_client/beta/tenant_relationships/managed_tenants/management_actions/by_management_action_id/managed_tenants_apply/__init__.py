# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.beta.managed_tenants_apply_post_request import Managed_tenants_applyPostRequest
from iograph_models.beta.managed_tenants_management_action_deployment_status import ManagedTenantsManagementActionDeploymentStatus
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ManagedTenantsApplyRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/tenantRelationships/managedTenants/managementActions/{managementAction%2Did}/microsoft.graph.managedTenants.apply", path_parameters)

	async def post(
		self,
		body: Managed_tenants_applyPostRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ManagedTenantsManagementActionDeploymentStatus:
		"""
		Invoke action apply
		Applies a management action against a specific managed tenant. Performing this operation makes the appropriate configurations and creates the appropriate policies. For example, when applying the required multifactor authentication for admins, management action creates a Microsoft Entra Conditional Access policy that requires multifactor authentication for all users that are assigned an administrative directory role.
		Find more info here: https://learn.microsoft.com/graph/api/managedtenants-managementaction-apply?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, ManagedTenantsManagementActionDeploymentStatus, error_mapping)


	def with_url(self, raw_url: str) -> ManagedTenantsApplyRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ManagedTenantsApplyRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ManagedTenantsApplyRequest(self.request_adapter, self.path_parameters)

