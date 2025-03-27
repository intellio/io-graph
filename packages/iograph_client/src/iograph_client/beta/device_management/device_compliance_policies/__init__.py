# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .validate_compliance_script import ValidateComplianceScriptRequest
	from .set_scheduled_retire_state import SetScheduledRetireStateRequest
	from .refresh_device_compliance_report_summarization import RefreshDeviceComplianceReportSummarizationRequest
	from .has_payload_links import HasPayloadLinksRequest
	from .get_noncompliant_devices_to_retire import GetNoncompliantDevicesToRetireRequest
	from .get_devices_scheduled_to_retire import GetDevicesScheduledToRetireRequest
	from .count import CountRequest
	from .by_device_compliance_policy_id import ByDeviceCompliancePolicyIdRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.beta.device_compliance_policy import DeviceCompliancePolicy
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.device_compliance_policy_collection_response import DeviceCompliancePolicyCollectionResponse


class DeviceCompliancePoliciesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/deviceCompliancePolicies", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DeviceCompliancePolicyCollectionResponse:
		"""
		Get deviceCompliancePolicies from deviceManagement
		The device compliance policies.
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
		return await self.request_adapter.send_async(request_info, DeviceCompliancePolicyCollectionResponse, error_mapping)

	async def post(
		self,
		body: DeviceCompliancePolicy,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> DeviceCompliancePolicy:
		"""
		Create new navigation property to deviceCompliancePolicies for deviceManagement
		
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
		return await self.request_adapter.send_async(request_info, DeviceCompliancePolicy, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> DeviceCompliancePoliciesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: DeviceCompliancePoliciesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return DeviceCompliancePoliciesRequest(self.request_adapter, self.path_parameters)

	def by_device_compliance_policy_id(self,
		deviceCompliancePolicy_id: str,
	) -> ByDeviceCompliancePolicyIdRequest:
		if deviceCompliancePolicy_id is None:
			raise TypeError("deviceCompliancePolicy_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceCompliancePolicy%2Did"] =  deviceCompliancePolicy_id

		from .by_device_compliance_policy_id import ByDeviceCompliancePolicyIdRequest
		return ByDeviceCompliancePolicyIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

	@property
	def get_devices_scheduled_to_retire(self,
	) -> GetDevicesScheduledToRetireRequest:
		from .get_devices_scheduled_to_retire import GetDevicesScheduledToRetireRequest
		return GetDevicesScheduledToRetireRequest(self.request_adapter, self.path_parameters)

	@property
	def get_noncompliant_devices_to_retire(self,
	) -> GetNoncompliantDevicesToRetireRequest:
		from .get_noncompliant_devices_to_retire import GetNoncompliantDevicesToRetireRequest
		return GetNoncompliantDevicesToRetireRequest(self.request_adapter, self.path_parameters)

	@property
	def has_payload_links(self,
	) -> HasPayloadLinksRequest:
		from .has_payload_links import HasPayloadLinksRequest
		return HasPayloadLinksRequest(self.request_adapter, self.path_parameters)

	@property
	def refresh_device_compliance_report_summarization(self,
	) -> RefreshDeviceComplianceReportSummarizationRequest:
		from .refresh_device_compliance_report_summarization import RefreshDeviceComplianceReportSummarizationRequest
		return RefreshDeviceComplianceReportSummarizationRequest(self.request_adapter, self.path_parameters)

	@property
	def set_scheduled_retire_state(self,
	) -> SetScheduledRetireStateRequest:
		from .set_scheduled_retire_state import SetScheduledRetireStateRequest
		return SetScheduledRetireStateRequest(self.request_adapter, self.path_parameters)

	@property
	def validate_compliance_script(self,
	) -> ValidateComplianceScriptRequest:
		from .validate_compliance_script import ValidateComplianceScriptRequest
		return ValidateComplianceScriptRequest(self.request_adapter, self.path_parameters)

