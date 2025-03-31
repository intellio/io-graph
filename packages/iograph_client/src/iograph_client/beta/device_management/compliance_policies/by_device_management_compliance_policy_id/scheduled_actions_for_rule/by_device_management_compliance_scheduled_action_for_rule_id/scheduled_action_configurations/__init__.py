# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_device_management_compliance_action_item_id import ByDeviceManagementComplianceActionItemIdRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.beta.device_management_compliance_action_item import DeviceManagementComplianceActionItem
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.device_management_compliance_action_item_collection_response import DeviceManagementComplianceActionItemCollectionResponse


class ScheduledActionConfigurationsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/compliancePolicies/{deviceManagementCompliancePolicy%2Did}/scheduledActionsForRule/{deviceManagementComplianceScheduledActionForRule%2Did}/scheduledActionConfigurations", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DeviceManagementComplianceActionItemCollectionResponse:
		"""
		Get scheduledActionConfigurations from deviceManagement
		The list of scheduled action configurations for this compliance policy. This collection can contain a maximum of 100 elements.
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
		return await self.request_adapter.send_async(request_info, DeviceManagementComplianceActionItemCollectionResponse, error_mapping)

	async def post(
		self,
		body: DeviceManagementComplianceActionItem,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> DeviceManagementComplianceActionItem:
		"""
		Create new navigation property to scheduledActionConfigurations for deviceManagement
		
		"""
		tags = ['deviceManagement.deviceManagementCompliancePolicy']

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
		return await self.request_adapter.send_async(request_info, DeviceManagementComplianceActionItem, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> ScheduledActionConfigurationsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ScheduledActionConfigurationsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ScheduledActionConfigurationsRequest(self.request_adapter, self.path_parameters)

	def by_device_management_compliance_action_item_id(self,
		deviceManagementCompliancePolicy_id: str,
		deviceManagementComplianceScheduledActionForRule_id: str,
		deviceManagementComplianceActionItem_id: str,
	) -> ByDeviceManagementComplianceActionItemIdRequest:
		if deviceManagementCompliancePolicy_id is None:
			raise TypeError("deviceManagementCompliancePolicy_id cannot be null.")
		if deviceManagementComplianceScheduledActionForRule_id is None:
			raise TypeError("deviceManagementComplianceScheduledActionForRule_id cannot be null.")
		if deviceManagementComplianceActionItem_id is None:
			raise TypeError("deviceManagementComplianceActionItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceManagementCompliancePolicy%2Did"] =  deviceManagementCompliancePolicy_id
		path_parameters["deviceManagementComplianceScheduledActionForRule%2Did"] =  deviceManagementComplianceScheduledActionForRule_id
		path_parameters["deviceManagementComplianceActionItem%2Did"] =  deviceManagementComplianceActionItem_id

		from .by_device_management_compliance_action_item_id import ByDeviceManagementComplianceActionItemIdRequest
		return ByDeviceManagementComplianceActionItemIdRequest(self.request_adapter, path_parameters)

	def count(self,
		deviceManagementCompliancePolicy_id: str,
		deviceManagementComplianceScheduledActionForRule_id: str,
	) -> CountRequest:
		if deviceManagementCompliancePolicy_id is None:
			raise TypeError("deviceManagementCompliancePolicy_id cannot be null.")
		if deviceManagementComplianceScheduledActionForRule_id is None:
			raise TypeError("deviceManagementComplianceScheduledActionForRule_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceManagementCompliancePolicy%2Did"] =  deviceManagementCompliancePolicy_id
		path_parameters["deviceManagementComplianceScheduledActionForRule%2Did"] =  deviceManagementComplianceScheduledActionForRule_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

