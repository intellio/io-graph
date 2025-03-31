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
	from .by_device_compliance_scheduled_action_for_rule_id import ByDeviceComplianceScheduledActionForRuleIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.device_compliance_scheduled_action_for_rule_collection_response import DeviceComplianceScheduledActionForRuleCollectionResponse
from iograph_models.beta.device_compliance_scheduled_action_for_rule import DeviceComplianceScheduledActionForRule
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ScheduledActionsForRuleRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/deviceCompliancePolicies/{deviceCompliancePolicy%2Did}/scheduledActionsForRule", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DeviceComplianceScheduledActionForRuleCollectionResponse:
		"""
		Get scheduledActionsForRule from deviceManagement
		The list of scheduled action per rule for this compliance policy. This is a required property when creating any individual per-platform compliance policies.
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
		return await self.request_adapter.send_async(request_info, DeviceComplianceScheduledActionForRuleCollectionResponse, error_mapping)

	async def post(
		self,
		body: DeviceComplianceScheduledActionForRule,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> DeviceComplianceScheduledActionForRule:
		"""
		Create new navigation property to scheduledActionsForRule for deviceManagement
		
		"""
		tags = ['deviceManagement.deviceCompliancePolicy']

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
		return await self.request_adapter.send_async(request_info, DeviceComplianceScheduledActionForRule, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> ScheduledActionsForRuleRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ScheduledActionsForRuleRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ScheduledActionsForRuleRequest(self.request_adapter, self.path_parameters)

	def by_device_compliance_scheduled_action_for_rule_id(self,
		deviceCompliancePolicy_id: str,
		deviceComplianceScheduledActionForRule_id: str,
	) -> ByDeviceComplianceScheduledActionForRuleIdRequest:
		if deviceCompliancePolicy_id is None:
			raise TypeError("deviceCompliancePolicy_id cannot be null.")
		if deviceComplianceScheduledActionForRule_id is None:
			raise TypeError("deviceComplianceScheduledActionForRule_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceCompliancePolicy%2Did"] =  deviceCompliancePolicy_id
		path_parameters["deviceComplianceScheduledActionForRule%2Did"] =  deviceComplianceScheduledActionForRule_id

		from .by_device_compliance_scheduled_action_for_rule_id import ByDeviceComplianceScheduledActionForRuleIdRequest
		return ByDeviceComplianceScheduledActionForRuleIdRequest(self.request_adapter, path_parameters)

	def count(self,
		deviceCompliancePolicy_id: str,
	) -> CountRequest:
		if deviceCompliancePolicy_id is None:
			raise TypeError("deviceCompliancePolicy_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceCompliancePolicy%2Did"] =  deviceCompliancePolicy_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

