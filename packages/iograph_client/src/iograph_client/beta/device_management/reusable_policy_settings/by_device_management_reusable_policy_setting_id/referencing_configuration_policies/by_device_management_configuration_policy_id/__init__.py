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
	from .settings import SettingsRequest
	from .set_enrollment_time_device_membership_target import SetEnrollmentTimeDeviceMembershipTargetRequest
	from .retrieve_latest_upgrade_default_baseline_policy import RetrieveLatestUpgradeDefaultBaselinePolicyRequest
	from .retrieve_enrollment_time_device_membership_target import RetrieveEnrollmentTimeDeviceMembershipTargetRequest
	from .reorder import ReorderRequest
	from .create_copy import CreateCopyRequest
	from .clear_enrollment_time_device_membership_target import ClearEnrollmentTimeDeviceMembershipTargetRequest
	from .assign import AssignRequest
	from .assignments import AssignmentsRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.beta.device_management_configuration_policy import DeviceManagementConfigurationPolicy
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByDeviceManagementConfigurationPolicyIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/reusablePolicySettings/{deviceManagementReusablePolicySetting%2Did}/referencingConfigurationPolicies/{deviceManagementConfigurationPolicy%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DeviceManagementConfigurationPolicy:
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
		return await self.request_adapter.send_async(request_info, DeviceManagementConfigurationPolicy, error_mapping)

	async def patch(
		self,
		body: DeviceManagementConfigurationPolicy,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> DeviceManagementConfigurationPolicy:
		"""
		Update the navigation property referencingConfigurationPolicies in deviceManagement
		
		"""
		tags = ['deviceManagement.deviceManagementReusablePolicySetting']

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
		return await self.request_adapter.send_async(request_info, DeviceManagementConfigurationPolicy, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property referencingConfigurationPolicies for deviceManagement
		
		"""
		tags = ['deviceManagement.deviceManagementReusablePolicySetting']
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



	def with_url(self, raw_url: str) -> ByDeviceManagementConfigurationPolicyIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByDeviceManagementConfigurationPolicyIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByDeviceManagementConfigurationPolicyIdRequest(self.request_adapter, self.path_parameters)

	def assignments(self,
		deviceManagementReusablePolicySetting_id: str,
		deviceManagementConfigurationPolicy_id: str,
	) -> AssignmentsRequest:
		if deviceManagementReusablePolicySetting_id is None:
			raise TypeError("deviceManagementReusablePolicySetting_id cannot be null.")
		if deviceManagementConfigurationPolicy_id is None:
			raise TypeError("deviceManagementConfigurationPolicy_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceManagementReusablePolicySetting%2Did"] =  deviceManagementReusablePolicySetting_id
		path_parameters["deviceManagementConfigurationPolicy%2Did"] =  deviceManagementConfigurationPolicy_id

		from .assignments import AssignmentsRequest
		return AssignmentsRequest(self.request_adapter, path_parameters)

	def assign(self,
		deviceManagementReusablePolicySetting_id: str,
		deviceManagementConfigurationPolicy_id: str,
	) -> AssignRequest:
		if deviceManagementReusablePolicySetting_id is None:
			raise TypeError("deviceManagementReusablePolicySetting_id cannot be null.")
		if deviceManagementConfigurationPolicy_id is None:
			raise TypeError("deviceManagementConfigurationPolicy_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceManagementReusablePolicySetting%2Did"] =  deviceManagementReusablePolicySetting_id
		path_parameters["deviceManagementConfigurationPolicy%2Did"] =  deviceManagementConfigurationPolicy_id

		from .assign import AssignRequest
		return AssignRequest(self.request_adapter, path_parameters)

	def clear_enrollment_time_device_membership_target(self,
		deviceManagementReusablePolicySetting_id: str,
		deviceManagementConfigurationPolicy_id: str,
	) -> ClearEnrollmentTimeDeviceMembershipTargetRequest:
		if deviceManagementReusablePolicySetting_id is None:
			raise TypeError("deviceManagementReusablePolicySetting_id cannot be null.")
		if deviceManagementConfigurationPolicy_id is None:
			raise TypeError("deviceManagementConfigurationPolicy_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceManagementReusablePolicySetting%2Did"] =  deviceManagementReusablePolicySetting_id
		path_parameters["deviceManagementConfigurationPolicy%2Did"] =  deviceManagementConfigurationPolicy_id

		from .clear_enrollment_time_device_membership_target import ClearEnrollmentTimeDeviceMembershipTargetRequest
		return ClearEnrollmentTimeDeviceMembershipTargetRequest(self.request_adapter, path_parameters)

	def create_copy(self,
		deviceManagementReusablePolicySetting_id: str,
		deviceManagementConfigurationPolicy_id: str,
	) -> CreateCopyRequest:
		if deviceManagementReusablePolicySetting_id is None:
			raise TypeError("deviceManagementReusablePolicySetting_id cannot be null.")
		if deviceManagementConfigurationPolicy_id is None:
			raise TypeError("deviceManagementConfigurationPolicy_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceManagementReusablePolicySetting%2Did"] =  deviceManagementReusablePolicySetting_id
		path_parameters["deviceManagementConfigurationPolicy%2Did"] =  deviceManagementConfigurationPolicy_id

		from .create_copy import CreateCopyRequest
		return CreateCopyRequest(self.request_adapter, path_parameters)

	def reorder(self,
		deviceManagementReusablePolicySetting_id: str,
		deviceManagementConfigurationPolicy_id: str,
	) -> ReorderRequest:
		if deviceManagementReusablePolicySetting_id is None:
			raise TypeError("deviceManagementReusablePolicySetting_id cannot be null.")
		if deviceManagementConfigurationPolicy_id is None:
			raise TypeError("deviceManagementConfigurationPolicy_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceManagementReusablePolicySetting%2Did"] =  deviceManagementReusablePolicySetting_id
		path_parameters["deviceManagementConfigurationPolicy%2Did"] =  deviceManagementConfigurationPolicy_id

		from .reorder import ReorderRequest
		return ReorderRequest(self.request_adapter, path_parameters)

	def retrieve_enrollment_time_device_membership_target(self,
		deviceManagementReusablePolicySetting_id: str,
		deviceManagementConfigurationPolicy_id: str,
	) -> RetrieveEnrollmentTimeDeviceMembershipTargetRequest:
		if deviceManagementReusablePolicySetting_id is None:
			raise TypeError("deviceManagementReusablePolicySetting_id cannot be null.")
		if deviceManagementConfigurationPolicy_id is None:
			raise TypeError("deviceManagementConfigurationPolicy_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceManagementReusablePolicySetting%2Did"] =  deviceManagementReusablePolicySetting_id
		path_parameters["deviceManagementConfigurationPolicy%2Did"] =  deviceManagementConfigurationPolicy_id

		from .retrieve_enrollment_time_device_membership_target import RetrieveEnrollmentTimeDeviceMembershipTargetRequest
		return RetrieveEnrollmentTimeDeviceMembershipTargetRequest(self.request_adapter, path_parameters)

	def retrieve_latest_upgrade_default_baseline_policy(self,
		deviceManagementReusablePolicySetting_id: str,
		deviceManagementConfigurationPolicy_id: str,
	) -> RetrieveLatestUpgradeDefaultBaselinePolicyRequest:
		if deviceManagementReusablePolicySetting_id is None:
			raise TypeError("deviceManagementReusablePolicySetting_id cannot be null.")
		if deviceManagementConfigurationPolicy_id is None:
			raise TypeError("deviceManagementConfigurationPolicy_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceManagementReusablePolicySetting%2Did"] =  deviceManagementReusablePolicySetting_id
		path_parameters["deviceManagementConfigurationPolicy%2Did"] =  deviceManagementConfigurationPolicy_id

		from .retrieve_latest_upgrade_default_baseline_policy import RetrieveLatestUpgradeDefaultBaselinePolicyRequest
		return RetrieveLatestUpgradeDefaultBaselinePolicyRequest(self.request_adapter, path_parameters)

	def set_enrollment_time_device_membership_target(self,
		deviceManagementReusablePolicySetting_id: str,
		deviceManagementConfigurationPolicy_id: str,
	) -> SetEnrollmentTimeDeviceMembershipTargetRequest:
		if deviceManagementReusablePolicySetting_id is None:
			raise TypeError("deviceManagementReusablePolicySetting_id cannot be null.")
		if deviceManagementConfigurationPolicy_id is None:
			raise TypeError("deviceManagementConfigurationPolicy_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceManagementReusablePolicySetting%2Did"] =  deviceManagementReusablePolicySetting_id
		path_parameters["deviceManagementConfigurationPolicy%2Did"] =  deviceManagementConfigurationPolicy_id

		from .set_enrollment_time_device_membership_target import SetEnrollmentTimeDeviceMembershipTargetRequest
		return SetEnrollmentTimeDeviceMembershipTargetRequest(self.request_adapter, path_parameters)

	def settings(self,
		deviceManagementReusablePolicySetting_id: str,
		deviceManagementConfigurationPolicy_id: str,
	) -> SettingsRequest:
		if deviceManagementReusablePolicySetting_id is None:
			raise TypeError("deviceManagementReusablePolicySetting_id cannot be null.")
		if deviceManagementConfigurationPolicy_id is None:
			raise TypeError("deviceManagementConfigurationPolicy_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceManagementReusablePolicySetting%2Did"] =  deviceManagementReusablePolicySetting_id
		path_parameters["deviceManagementConfigurationPolicy%2Did"] =  deviceManagementConfigurationPolicy_id

		from .settings import SettingsRequest
		return SettingsRequest(self.request_adapter, path_parameters)

