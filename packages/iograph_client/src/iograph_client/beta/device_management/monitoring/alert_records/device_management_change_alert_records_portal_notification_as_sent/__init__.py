# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.device_management_change_alert_records_portal_notification_as_sent_post_request import Device_management_change_alert_records_portal_notification_as_sentPostRequest


class DeviceManagementChangeAlertRecordsPortalNotificationAsSentRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/monitoring/alertRecords/microsoft.graph.deviceManagement.changeAlertRecordsPortalNotificationAsSent", path_parameters)

	async def post(
		self,
		body: Device_management_change_alert_records_portal_notification_as_sentPostRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Invoke action changeAlertRecordsPortalNotificationAsSent
		Set the isPortalNotificationSent property of all portal notification resources associated with the specified alertRecord to true, marking them as sent. A maximum of 100 alertRecord IDs can be received at one time, and a maximum of 100 portal notification resources can be changed in the isPortalNotificationSent property status.
		"""
		tags = ['deviceManagement.monitoring']

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
		return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)


	def with_url(self, raw_url: str) -> DeviceManagementChangeAlertRecordsPortalNotificationAsSentRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: DeviceManagementChangeAlertRecordsPortalNotificationAsSentRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return DeviceManagementChangeAlertRecordsPortalNotificationAsSentRequest(self.request_adapter, self.path_parameters)

