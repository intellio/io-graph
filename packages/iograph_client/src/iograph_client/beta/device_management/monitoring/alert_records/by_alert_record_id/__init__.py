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
	from .device_management_set_portal_notification_as_sent import DeviceManagementSetPortalNotificationAsSentRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.device_management_alert_record import DeviceManagementAlertRecord


class ByAlertRecordIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/monitoring/alertRecords/{alertRecord%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DeviceManagementAlertRecord:
		"""
		Get alertRecord
		Read the properties and relationships of an alertRecord object.
		Find more info here: https://learn.microsoft.com/graph/api/devicemanagement-alertrecord-get?view=graph-rest-beta
		"""
		tags = ['deviceManagement.monitoring']

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
		return await self.request_adapter.send_async(request_info, DeviceManagementAlertRecord, error_mapping)

	async def patch(
		self,
		body: DeviceManagementAlertRecord,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> DeviceManagementAlertRecord:
		"""
		Update the navigation property alertRecords in deviceManagement
		
		"""
		tags = ['deviceManagement.monitoring']

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
		return await self.request_adapter.send_async(request_info, DeviceManagementAlertRecord, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property alertRecords for deviceManagement
		
		"""
		tags = ['deviceManagement.monitoring']
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



	def with_url(self, raw_url: str) -> ByAlertRecordIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByAlertRecordIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByAlertRecordIdRequest(self.request_adapter, self.path_parameters)

	def device_management_set_portal_notification_as_sent(self,
		alertRecord_id: str,
	) -> DeviceManagementSetPortalNotificationAsSentRequest:
		if alertRecord_id is None:
			raise TypeError("alertRecord_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["alertRecord%2Did"] =  alertRecord_id

		from .device_management_set_portal_notification_as_sent import DeviceManagementSetPortalNotificationAsSentRequest
		return DeviceManagementSetPortalNotificationAsSentRequest(self.request_adapter, path_parameters)

