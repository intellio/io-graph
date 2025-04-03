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
	from .count import CountRequest
	from .by_device_management_configuration_policy_id import ByDeviceManagementConfigurationPolicyIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.device_management_configuration_policy import DeviceManagementConfigurationPolicy
from iograph_models.beta.device_management_configuration_policy_collection_response import DeviceManagementConfigurationPolicyCollectionResponse


class ReferencingConfigurationPoliciesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/reusablePolicySettings/{deviceManagementReusablePolicySetting%2Did}/referencingConfigurationPolicies", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DeviceManagementConfigurationPolicyCollectionResponse:
		"""
		Get referencingConfigurationPolicies from deviceManagement
		configuration policies referencing the current reusable setting. This property is read-only.
		"""
		tags = ['deviceManagement.deviceManagementReusablePolicySetting']

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
		return await self.request_adapter.send_async(request_info, DeviceManagementConfigurationPolicyCollectionResponse, error_mapping)

	async def post(
		self,
		body: DeviceManagementConfigurationPolicy,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> DeviceManagementConfigurationPolicy:
		"""
		Create new navigation property to referencingConfigurationPolicies for deviceManagement
		
		"""
		tags = ['deviceManagement.deviceManagementReusablePolicySetting']

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
		return await self.request_adapter.send_async(request_info, DeviceManagementConfigurationPolicy, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> ReferencingConfigurationPoliciesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ReferencingConfigurationPoliciesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ReferencingConfigurationPoliciesRequest(self.request_adapter, self.path_parameters)

	def by_device_management_configuration_policy_id(self,
		deviceManagementReusablePolicySetting_id: str,
		deviceManagementConfigurationPolicy_id: str,
	) -> ByDeviceManagementConfigurationPolicyIdRequest:
		if deviceManagementReusablePolicySetting_id is None:
			raise TypeError("deviceManagementReusablePolicySetting_id cannot be null.")
		if deviceManagementConfigurationPolicy_id is None:
			raise TypeError("deviceManagementConfigurationPolicy_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceManagementReusablePolicySetting%2Did"] =  deviceManagementReusablePolicySetting_id
		path_parameters["deviceManagementConfigurationPolicy%2Did"] =  deviceManagementConfigurationPolicy_id

		from .by_device_management_configuration_policy_id import ByDeviceManagementConfigurationPolicyIdRequest
		return ByDeviceManagementConfigurationPolicyIdRequest(self.request_adapter, path_parameters)

	def count(self,
		deviceManagementReusablePolicySetting_id: str,
	) -> CountRequest:
		if deviceManagementReusablePolicySetting_id is None:
			raise TypeError("deviceManagementReusablePolicySetting_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceManagementReusablePolicySetting%2Did"] =  deviceManagementReusablePolicySetting_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

