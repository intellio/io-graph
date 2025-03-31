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
	from .scheduled_action_configurations import ScheduledActionConfigurationsRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.beta.device_management_compliance_scheduled_action_for_rule import DeviceManagementComplianceScheduledActionForRule
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByDeviceManagementComplianceScheduledActionForRuleIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/compliancePolicies/{deviceManagementCompliancePolicy%2Did}/scheduledActionsForRule/{deviceManagementComplianceScheduledActionForRule%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DeviceManagementComplianceScheduledActionForRule:
		"""
		Get scheduledActionsForRule from deviceManagement
		The list of scheduled action for this rule
		"""
		tags = ['deviceManagement.deviceManagementCompliancePolicy']

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
		return await self.request_adapter.send_async(request_info, DeviceManagementComplianceScheduledActionForRule, error_mapping)

	async def patch(
		self,
		body: DeviceManagementComplianceScheduledActionForRule,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> DeviceManagementComplianceScheduledActionForRule:
		"""
		Update the navigation property scheduledActionsForRule in deviceManagement
		
		"""
		tags = ['deviceManagement.deviceManagementCompliancePolicy']

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
		return await self.request_adapter.send_async(request_info, DeviceManagementComplianceScheduledActionForRule, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property scheduledActionsForRule for deviceManagement
		
		"""
		tags = ['deviceManagement.deviceManagementCompliancePolicy']
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



	def with_url(self, raw_url: str) -> ByDeviceManagementComplianceScheduledActionForRuleIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByDeviceManagementComplianceScheduledActionForRuleIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByDeviceManagementComplianceScheduledActionForRuleIdRequest(self.request_adapter, self.path_parameters)

	def scheduled_action_configurations(self,
		deviceManagementCompliancePolicy_id: str,
		deviceManagementComplianceScheduledActionForRule_id: str,
	) -> ScheduledActionConfigurationsRequest:
		if deviceManagementCompliancePolicy_id is None:
			raise TypeError("deviceManagementCompliancePolicy_id cannot be null.")
		if deviceManagementComplianceScheduledActionForRule_id is None:
			raise TypeError("deviceManagementComplianceScheduledActionForRule_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceManagementCompliancePolicy%2Did"] =  deviceManagementCompliancePolicy_id
		path_parameters["deviceManagementComplianceScheduledActionForRule%2Did"] =  deviceManagementComplianceScheduledActionForRule_id

		from .scheduled_action_configurations import ScheduledActionConfigurationsRequest
		return ScheduledActionConfigurationsRequest(self.request_adapter, path_parameters)

