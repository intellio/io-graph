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
	from .count import CountRequest
	from .by_cloud_pc_provisioning_policy_assignment_id import ByCloudPcProvisioningPolicyAssignmentIdRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.v1.cloud_pc_provisioning_policy_assignment_collection_response import CloudPcProvisioningPolicyAssignmentCollectionResponse
from iograph_models.v1.cloud_pc_provisioning_policy_assignment import CloudPcProvisioningPolicyAssignment


class AssignmentsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/virtualEndpoint/provisioningPolicies/{cloudPcProvisioningPolicy%2Did}/assignments", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> CloudPcProvisioningPolicyAssignmentCollectionResponse:
		"""
		Get assignments from deviceManagement
		A defined collection of provisioning policy assignments. Represents the set of Microsoft 365 groups and security groups in Microsoft Entra ID that have provisioning policy assigned. Returned only on $expand. For an example about how to get the assignments relationship, see Get cloudPcProvisioningPolicy.
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
		return await self.request_adapter.send_async(request_info, CloudPcProvisioningPolicyAssignmentCollectionResponse, error_mapping)

	async def post(
		self,
		body: CloudPcProvisioningPolicyAssignment,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> CloudPcProvisioningPolicyAssignment:
		"""
		Create new navigation property to assignments for deviceManagement
		
		"""
		tags = ['deviceManagement.virtualEndpoint']

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
		return await self.request_adapter.send_async(request_info, CloudPcProvisioningPolicyAssignment, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> AssignmentsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: AssignmentsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return AssignmentsRequest(self.request_adapter, self.path_parameters)

	def by_cloud_pc_provisioning_policy_assignment_id(self,
		cloudPcProvisioningPolicy_id: str,
		cloudPcProvisioningPolicyAssignment_id: str,
	) -> ByCloudPcProvisioningPolicyAssignmentIdRequest:
		if cloudPcProvisioningPolicy_id is None:
			raise TypeError("cloudPcProvisioningPolicy_id cannot be null.")
		if cloudPcProvisioningPolicyAssignment_id is None:
			raise TypeError("cloudPcProvisioningPolicyAssignment_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["cloudPcProvisioningPolicy%2Did"] =  cloudPcProvisioningPolicy_id
		path_parameters["cloudPcProvisioningPolicyAssignment%2Did"] =  cloudPcProvisioningPolicyAssignment_id

		from .by_cloud_pc_provisioning_policy_assignment_id import ByCloudPcProvisioningPolicyAssignmentIdRequest
		return ByCloudPcProvisioningPolicyAssignmentIdRequest(self.request_adapter, path_parameters)

	def count(self,
		cloudPcProvisioningPolicy_id: str,
	) -> CountRequest:
		if cloudPcProvisioningPolicy_id is None:
			raise TypeError("cloudPcProvisioningPolicy_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["cloudPcProvisioningPolicy%2Did"] =  cloudPcProvisioningPolicy_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

