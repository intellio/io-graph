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
	from .count import CountRequest
	from .by_notification_message_template_id import ByNotificationMessageTemplateIdRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.v1.notification_message_template import NotificationMessageTemplate
from iograph_models.v1.notification_message_template_collection_response import NotificationMessageTemplateCollectionResponse
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class NotificationMessageTemplatesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/notificationMessageTemplates", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> NotificationMessageTemplateCollectionResponse:
		"""
		List notificationMessageTemplates
		List properties and relationships of the notificationMessageTemplate objects.
		Find more info here: https://learn.microsoft.com/graph/api/intune-notification-notificationmessagetemplate-list?view=graph-rest-1.0
		"""
		tags = ['deviceManagement.notificationMessageTemplate']

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
		return await self.request_adapter.send_async(request_info, NotificationMessageTemplateCollectionResponse, error_mapping)

	async def post(
		self,
		body: NotificationMessageTemplate,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> NotificationMessageTemplate:
		"""
		Create notificationMessageTemplate
		Create a new notificationMessageTemplate object.
		Find more info here: https://learn.microsoft.com/graph/api/intune-notification-notificationmessagetemplate-create?view=graph-rest-1.0
		"""
		tags = ['deviceManagement.notificationMessageTemplate']

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
		return await self.request_adapter.send_async(request_info, NotificationMessageTemplate, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> NotificationMessageTemplatesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: NotificationMessageTemplatesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return NotificationMessageTemplatesRequest(self.request_adapter, self.path_parameters)

	def by_notification_message_template_id(self,
		notificationMessageTemplate_id: str,
	) -> ByNotificationMessageTemplateIdRequest:
		if notificationMessageTemplate_id is None:
			raise TypeError("notificationMessageTemplate_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["notificationMessageTemplate%2Did"] =  notificationMessageTemplate_id

		from .by_notification_message_template_id import ByNotificationMessageTemplateIdRequest
		return ByNotificationMessageTemplateIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

