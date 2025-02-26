# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
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


class ByDeviceCompliancePolicyIdRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/deviceManagement/deviceCompliancePolicies/{deviceCompliancePolicy%2Did}"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DeviceCompliancePolicy:
		"""
		Get deviceCompliancePolicy
		Read properties and relationships of the deviceCompliancePolicy object.
		Find more info here: https://learn.microsoft.com/graph/api/intune-deviceconfig-devicecompliancepolicy-get?view=graph-rest-1.0
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
		Update androidCompliancePolicy
		Update the properties of a androidCompliancePolicy object.
		Find more info here: https://learn.microsoft.com/graph/api/intune-deviceconfig-androidcompliancepolicy-update?view=graph-rest-1.0
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
		Delete iosCompliancePolicy
		Deletes a iosCompliancePolicy.
		Find more info here: https://learn.microsoft.com/graph/api/intune-deviceconfig-ioscompliancepolicy-delete?view=graph-rest-1.0
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



	@property
	def assignments(self,
	) -> AssignmentsRequest:
		from .assignments import AssignmentsRequest
		return AssignmentsRequest(self.request_adapter, self.path_parameters)

	@property
	def device_setting_state_summaries(self,
	) -> DeviceSettingStateSummariesRequest:
		from .device_setting_state_summaries import DeviceSettingStateSummariesRequest
		return DeviceSettingStateSummariesRequest(self.request_adapter, self.path_parameters)

	@property
	def device_statuses(self,
	) -> DeviceStatusesRequest:
		from .device_statuses import DeviceStatusesRequest
		return DeviceStatusesRequest(self.request_adapter, self.path_parameters)

	@property
	def device_status_overview(self,
	) -> DeviceStatusOverviewRequest:
		from .device_status_overview import DeviceStatusOverviewRequest
		return DeviceStatusOverviewRequest(self.request_adapter, self.path_parameters)

	@property
	def assign(self,
	) -> AssignRequest:
		from .assign import AssignRequest
		return AssignRequest(self.request_adapter, self.path_parameters)

	@property
	def schedule_actions_for_rules(self,
	) -> ScheduleActionsForRulesRequest:
		from .schedule_actions_for_rules import ScheduleActionsForRulesRequest
		return ScheduleActionsForRulesRequest(self.request_adapter, self.path_parameters)

	@property
	def scheduled_actions_for_rule(self,
	) -> ScheduledActionsForRuleRequest:
		from .scheduled_actions_for_rule import ScheduledActionsForRuleRequest
		return ScheduledActionsForRuleRequest(self.request_adapter, self.path_parameters)

	@property
	def user_statuses(self,
	) -> UserStatusesRequest:
		from .user_statuses import UserStatusesRequest
		return UserStatusesRequest(self.request_adapter, self.path_parameters)

	@property
	def user_status_overview(self,
	) -> UserStatusOverviewRequest:
		from .user_status_overview import UserStatusOverviewRequest
		return UserStatusOverviewRequest(self.request_adapter, self.path_parameters)

