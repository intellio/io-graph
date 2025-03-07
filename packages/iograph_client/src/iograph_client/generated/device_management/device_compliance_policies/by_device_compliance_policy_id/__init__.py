# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .user_status_overview import UserStatusOverviewRequest
	from .user_statuses import UserStatusesRequest
	from .scheduled_actions_for_rule import ScheduledActionsForRuleRequest
	from .schedule_actions_for_rules import ScheduleActionsForRulesRequest
	from .assign import AssignRequest
	from .device_status_overview import DeviceStatusOverviewRequest
	from .device_statuses import DeviceStatusesRequest
	from .device_setting_state_summaries import DeviceSettingStateSummariesRequest
	from .assignments import AssignmentsRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.models.device_compliance_policy import DeviceCompliancePolicy
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByDeviceCompliancePolicyIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/deviceCompliancePolicies/{deviceCompliancePolicy%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DeviceCompliancePolicy:
		"""
		Get windows10MobileCompliancePolicy
		Read properties and relationships of the windows10MobileCompliancePolicy object.
		Find more info here: https://learn.microsoft.com/graph/api/intune-deviceconfig-windows10mobilecompliancepolicy-get?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, DeviceCompliancePolicy, error_mapping)

	async def patch(
		self,
		body: DeviceCompliancePolicy,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> DeviceCompliancePolicy:
		"""
		Update iosCompliancePolicy
		Update the properties of a iosCompliancePolicy object.
		Find more info here: https://learn.microsoft.com/graph/api/intune-deviceconfig-ioscompliancepolicy-update?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, DeviceCompliancePolicy, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete windows81CompliancePolicy
		Deletes a windows81CompliancePolicy.
		Find more info here: https://learn.microsoft.com/graph/api/intune-deviceconfig-windows81compliancepolicy-delete?view=graph-rest-1.0
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



	def with_url(self, raw_url: str) -> ByDeviceCompliancePolicyIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByDeviceCompliancePolicyIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByDeviceCompliancePolicyIdRequest(self.request_adapter, self.path_parameters)

	def assignments(self,
		deviceCompliancePolicy_id: str,
	) -> AssignmentsRequest:
		if deviceCompliancePolicy_id is None:
			raise TypeError("deviceCompliancePolicy_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceCompliancePolicy%2Did"] =  deviceCompliancePolicy_id

		from .assignments import AssignmentsRequest
		return AssignmentsRequest(self.request_adapter, path_parameters)

	def device_setting_state_summaries(self,
		deviceCompliancePolicy_id: str,
	) -> DeviceSettingStateSummariesRequest:
		if deviceCompliancePolicy_id is None:
			raise TypeError("deviceCompliancePolicy_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceCompliancePolicy%2Did"] =  deviceCompliancePolicy_id

		from .device_setting_state_summaries import DeviceSettingStateSummariesRequest
		return DeviceSettingStateSummariesRequest(self.request_adapter, path_parameters)

	def device_statuses(self,
		deviceCompliancePolicy_id: str,
	) -> DeviceStatusesRequest:
		if deviceCompliancePolicy_id is None:
			raise TypeError("deviceCompliancePolicy_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceCompliancePolicy%2Did"] =  deviceCompliancePolicy_id

		from .device_statuses import DeviceStatusesRequest
		return DeviceStatusesRequest(self.request_adapter, path_parameters)

	def device_status_overview(self,
		deviceCompliancePolicy_id: str,
	) -> DeviceStatusOverviewRequest:
		if deviceCompliancePolicy_id is None:
			raise TypeError("deviceCompliancePolicy_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceCompliancePolicy%2Did"] =  deviceCompliancePolicy_id

		from .device_status_overview import DeviceStatusOverviewRequest
		return DeviceStatusOverviewRequest(self.request_adapter, path_parameters)

	def assign(self,
		deviceCompliancePolicy_id: str,
	) -> AssignRequest:
		if deviceCompliancePolicy_id is None:
			raise TypeError("deviceCompliancePolicy_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceCompliancePolicy%2Did"] =  deviceCompliancePolicy_id

		from .assign import AssignRequest
		return AssignRequest(self.request_adapter, path_parameters)

	def schedule_actions_for_rules(self,
		deviceCompliancePolicy_id: str,
	) -> ScheduleActionsForRulesRequest:
		if deviceCompliancePolicy_id is None:
			raise TypeError("deviceCompliancePolicy_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceCompliancePolicy%2Did"] =  deviceCompliancePolicy_id

		from .schedule_actions_for_rules import ScheduleActionsForRulesRequest
		return ScheduleActionsForRulesRequest(self.request_adapter, path_parameters)

	def scheduled_actions_for_rule(self,
		deviceCompliancePolicy_id: str,
	) -> ScheduledActionsForRuleRequest:
		if deviceCompliancePolicy_id is None:
			raise TypeError("deviceCompliancePolicy_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceCompliancePolicy%2Did"] =  deviceCompliancePolicy_id

		from .scheduled_actions_for_rule import ScheduledActionsForRuleRequest
		return ScheduledActionsForRuleRequest(self.request_adapter, path_parameters)

	def user_statuses(self,
		deviceCompliancePolicy_id: str,
	) -> UserStatusesRequest:
		if deviceCompliancePolicy_id is None:
			raise TypeError("deviceCompliancePolicy_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceCompliancePolicy%2Did"] =  deviceCompliancePolicy_id

		from .user_statuses import UserStatusesRequest
		return UserStatusesRequest(self.request_adapter, path_parameters)

	def user_status_overview(self,
		deviceCompliancePolicy_id: str,
	) -> UserStatusOverviewRequest:
		if deviceCompliancePolicy_id is None:
			raise TypeError("deviceCompliancePolicy_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceCompliancePolicy%2Did"] =  deviceCompliancePolicy_id

		from .user_status_overview import UserStatusOverviewRequest
		return UserStatusOverviewRequest(self.request_adapter, path_parameters)

