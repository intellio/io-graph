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
from iograph_models.v1.device_compliance_scheduled_action_for_rule import DeviceComplianceScheduledActionForRule
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class ByDeviceComplianceScheduledActionForRuleIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/deviceCompliancePolicies/{deviceCompliancePolicy%2Did}/scheduledActionsForRule/{deviceComplianceScheduledActionForRule%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DeviceComplianceScheduledActionForRule:
		"""
		Get deviceComplianceScheduledActionForRule
		Read properties and relationships of the deviceComplianceScheduledActionForRule object.
		Find more info here: https://learn.microsoft.com/graph/api/intune-deviceconfig-devicecompliancescheduledactionforrule-get?view=graph-rest-1.0
		"""
		tags = ['deviceManagement.deviceCompliancePolicy']

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
		return await self.request_adapter.send_async(request_info, DeviceComplianceScheduledActionForRule, error_mapping)

	async def patch(
		self,
		body: DeviceComplianceScheduledActionForRule,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> DeviceComplianceScheduledActionForRule:
		"""
		Update deviceComplianceScheduledActionForRule
		Update the properties of a deviceComplianceScheduledActionForRule object.
		Find more info here: https://learn.microsoft.com/graph/api/intune-deviceconfig-devicecompliancescheduledactionforrule-update?view=graph-rest-1.0
		"""
		tags = ['deviceManagement.deviceCompliancePolicy']

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
		return await self.request_adapter.send_async(request_info, DeviceComplianceScheduledActionForRule, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete deviceComplianceScheduledActionForRule
		Deletes a deviceComplianceScheduledActionForRule.
		Find more info here: https://learn.microsoft.com/graph/api/intune-deviceconfig-devicecompliancescheduledactionforrule-delete?view=graph-rest-1.0
		"""
		tags = ['deviceManagement.deviceCompliancePolicy']
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



	def with_url(self, raw_url: str) -> ByDeviceComplianceScheduledActionForRuleIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByDeviceComplianceScheduledActionForRuleIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByDeviceComplianceScheduledActionForRuleIdRequest(self.request_adapter, self.path_parameters)

	def scheduled_action_configurations(self,
		deviceCompliancePolicy_id: str,
		deviceComplianceScheduledActionForRule_id: str,
	) -> ScheduledActionConfigurationsRequest:
		if deviceCompliancePolicy_id is None:
			raise TypeError("deviceCompliancePolicy_id cannot be null.")
		if deviceComplianceScheduledActionForRule_id is None:
			raise TypeError("deviceComplianceScheduledActionForRule_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceCompliancePolicy%2Did"] =  deviceCompliancePolicy_id
		path_parameters["deviceComplianceScheduledActionForRule%2Did"] =  deviceComplianceScheduledActionForRule_id

		from .scheduled_action_configurations import ScheduledActionConfigurationsRequest
		return ScheduledActionConfigurationsRequest(self.request_adapter, path_parameters)

