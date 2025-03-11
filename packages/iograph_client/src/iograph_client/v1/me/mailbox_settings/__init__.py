# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.v1.mailbox_settings import MailboxSettings


class MailboxSettingsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/me/mailboxSettings", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> MailboxSettings:
		"""
		Get user mailbox settings
		Get the user's mailboxSettings. You can view all mailbox settings, or get specific settings. Users can set the following settings for their mailboxes through an Outlook client: Users can set their preferred date and time formats using Outlook on the web. Users can choose one of the supported short date or short time formats. This GET operation returns the format the user has chosen. Users can set the time zone they prefer on any Outlook client, by choosing from the supported time zones that their administrator has set up for their mailbox server. The administrator can set up time zones in the Windows time zone format or  Internet Assigned Numbers Authority (IANA) time zone (also known as Olson time zone) format. The Windows format is the default. This GET operation returns the user's preferred time zone in the format that the administrator has set up. If you want that time zone to be in a specific format (Windows or IANA), you can first update the preferred time zone in that format as a mailbox setting. Subsequently you will be able to get the time zone in that format. Alternatively, you can manage the format conversion separately in your app.
		Find more info here: https://learn.microsoft.com/graph/api/user-get-mailboxsettings?view=graph-rest-1.0
		"""
		tags = ['me.mailboxSettings']

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
		return await self.request_adapter.send_async(request_info, MailboxSettings, error_mapping)

	async def patch(
		self,
		body: MailboxSettings,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> MailboxSettings:
		"""
		Update user mailbox settings
		Enable, configure, or disable one or more of the following settings as part of a user's mailboxSettings: When updating the preferred date or time format for a user, specify it in respectively, the short date or short time format. When updating the preferred time zone for a user, specify it in the Windows or Internet Assigned Numbers Authority (IANA) time zone (also known as Olson time zone) format. You can also further customize the time zone as shown in example 2 below.
		Find more info here: https://learn.microsoft.com/graph/api/user-update-mailboxsettings?view=graph-rest-1.0
		"""
		tags = ['me.mailboxSettings']

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
		return await self.request_adapter.send_async(request_info, MailboxSettings, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> MailboxSettingsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: MailboxSettingsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return MailboxSettingsRequest(self.request_adapter, self.path_parameters)

