# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ..........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .service_provisioning_errors import ServiceProvisioningErrorsRequest
	from .mailbox_settings import MailboxSettingsRequest
	from ..........request_adapter import HttpxRequestAdapter
from iograph_models.beta.user import User
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByUserIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/virtualEndpoint/provisioningPolicies/{cloudPcProvisioningPolicy%2Did}/assignments/{cloudPcProvisioningPolicyAssignment%2Did}/assignedUsers/{user%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> User:
		"""
		Get assignedUsers from deviceManagement
		The assignment targeted users for the provisioning policy. This list of users is computed based on assignments, licenses, group memberships, and policies. This property is read-only. Supports$expand.
		"""
		tags = ['deviceManagement.virtualEndpoint']

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
		return await self.request_adapter.send_async(request_info, User, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def with_url(self, raw_url: str) -> ByUserIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByUserIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByUserIdRequest(self.request_adapter, self.path_parameters)

	def mailbox_settings(self,
		cloudPcProvisioningPolicy_id: str,
		cloudPcProvisioningPolicyAssignment_id: str,
		user_id: str,
	) -> MailboxSettingsRequest:
		if cloudPcProvisioningPolicy_id is None:
			raise TypeError("cloudPcProvisioningPolicy_id cannot be null.")
		if cloudPcProvisioningPolicyAssignment_id is None:
			raise TypeError("cloudPcProvisioningPolicyAssignment_id cannot be null.")
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["cloudPcProvisioningPolicy%2Did"] =  cloudPcProvisioningPolicy_id
		path_parameters["cloudPcProvisioningPolicyAssignment%2Did"] =  cloudPcProvisioningPolicyAssignment_id
		path_parameters["user%2Did"] =  user_id

		from .mailbox_settings import MailboxSettingsRequest
		return MailboxSettingsRequest(self.request_adapter, path_parameters)

	def service_provisioning_errors(self,
		cloudPcProvisioningPolicy_id: str,
		cloudPcProvisioningPolicyAssignment_id: str,
		user_id: str,
	) -> ServiceProvisioningErrorsRequest:
		if cloudPcProvisioningPolicy_id is None:
			raise TypeError("cloudPcProvisioningPolicy_id cannot be null.")
		if cloudPcProvisioningPolicyAssignment_id is None:
			raise TypeError("cloudPcProvisioningPolicyAssignment_id cannot be null.")
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["cloudPcProvisioningPolicy%2Did"] =  cloudPcProvisioningPolicy_id
		path_parameters["cloudPcProvisioningPolicyAssignment%2Did"] =  cloudPcProvisioningPolicyAssignment_id
		path_parameters["user%2Did"] =  user_id

		from .service_provisioning_errors import ServiceProvisioningErrorsRequest
		return ServiceProvisioningErrorsRequest(self.request_adapter, path_parameters)

