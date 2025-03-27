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
	from .pronouns import PronounsRequest
	from .profile_card_properties import ProfileCardPropertiesRequest
	from .item_insights import ItemInsightsRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.v1.people_admin_settings import PeopleAdminSettings
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class PeopleRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/admin/people", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> PeopleAdminSettings:
		"""
		Get peopleAdminSettings
		Retrieve the properties and relationships of a peopleAdminSettings object.
		Find more info here: https://learn.microsoft.com/graph/api/peopleadminsettings-get?view=graph-rest-1.0
		"""
		tags = ['admin.peopleAdminSettings']

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
		return await self.request_adapter.send_async(request_info, PeopleAdminSettings, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def with_url(self, raw_url: str) -> PeopleRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: PeopleRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return PeopleRequest(self.request_adapter, self.path_parameters)

	@property
	def item_insights(self,
	) -> ItemInsightsRequest:
		from .item_insights import ItemInsightsRequest
		return ItemInsightsRequest(self.request_adapter, self.path_parameters)

	@property
	def profile_card_properties(self,
	) -> ProfileCardPropertiesRequest:
		from .profile_card_properties import ProfileCardPropertiesRequest
		return ProfileCardPropertiesRequest(self.request_adapter, self.path_parameters)

	@property
	def pronouns(self,
	) -> PronounsRequest:
		from .pronouns import PronounsRequest
		return PronounsRequest(self.request_adapter, self.path_parameters)

