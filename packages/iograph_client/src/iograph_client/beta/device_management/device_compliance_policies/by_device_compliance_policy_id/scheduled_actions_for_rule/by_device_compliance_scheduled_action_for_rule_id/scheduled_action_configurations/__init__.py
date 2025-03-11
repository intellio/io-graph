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
	from .by_device_compliance_action_item_id import ByDeviceComplianceActionItemIdRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.beta.device_compliance_action_item import DeviceComplianceActionItem
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.device_compliance_action_item_collection_response import DeviceComplianceActionItemCollectionResponse


class ScheduledActionConfigurationsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/deviceCompliancePolicies/{deviceCompliancePolicy%2Did}/scheduledActionsForRule/{deviceComplianceScheduledActionForRule%2Did}/scheduledActionConfigurations", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DeviceComplianceActionItemCollectionResponse:
		"""
		Get scheduledActionConfigurations from deviceManagement
		The list of scheduled action configurations for this compliance policy. Compliance policy must have one and only one block scheduled action.
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
		return await self.request_adapter.send_async(request_info, DeviceComplianceActionItemCollectionResponse, error_mapping)

	async def post(
		self,
		body: DeviceComplianceActionItem,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> DeviceComplianceActionItem:
		"""
		Create new navigation property to scheduledActionConfigurations for deviceManagement
		
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
		return await self.request_adapter.send_async(request_info, DeviceComplianceActionItem, error_mapping)

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

	def by_device_compliance_action_item_id(self,
		deviceCompliancePolicy_id: str,
		deviceComplianceScheduledActionForRule_id: str,
		deviceComplianceActionItem_id: str,
	) -> ByDeviceComplianceActionItemIdRequest:
		if deviceCompliancePolicy_id is None:
			raise TypeError("deviceCompliancePolicy_id cannot be null.")
		if deviceComplianceScheduledActionForRule_id is None:
			raise TypeError("deviceComplianceScheduledActionForRule_id cannot be null.")
		if deviceComplianceActionItem_id is None:
			raise TypeError("deviceComplianceActionItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceCompliancePolicy%2Did"] =  deviceCompliancePolicy_id
		path_parameters["deviceComplianceScheduledActionForRule%2Did"] =  deviceComplianceScheduledActionForRule_id
		path_parameters["deviceComplianceActionItem%2Did"] =  deviceComplianceActionItem_id

		from .by_device_compliance_action_item_id import ByDeviceComplianceActionItemIdRequest
		return ByDeviceComplianceActionItemIdRequest(self.request_adapter, path_parameters)

	def count(self,
		deviceCompliancePolicy_id: str,
		deviceComplianceScheduledActionForRule_id: str,
	) -> CountRequest:
		if deviceCompliancePolicy_id is None:
			raise TypeError("deviceCompliancePolicy_id cannot be null.")
		if deviceComplianceScheduledActionForRule_id is None:
			raise TypeError("deviceComplianceScheduledActionForRule_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceCompliancePolicy%2Did"] =  deviceCompliancePolicy_id
		path_parameters["deviceComplianceScheduledActionForRule%2Did"] =  deviceComplianceScheduledActionForRule_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

