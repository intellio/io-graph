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
	from .people_insights import PeopleInsightsRequest
	from .microsoft_application_data_access import MicrosoftApplicationDataAccessRequest
	from .item_insights import ItemInsightsRequest
	from .contact_insights import ContactInsightsRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.organization_settings import OrganizationSettings
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class SettingsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/organization/{organization%2Did}/settings", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> OrganizationSettings:
		"""
		Get settings from organization
		Retrieve the properties and relationships of organizationSettings object. Nullable.
		"""
		tags = ['organization.organizationSettings']

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
		return await self.request_adapter.send_async(request_info, OrganizationSettings, error_mapping)

	async def patch(
		self,
		body: OrganizationSettings,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> OrganizationSettings:
		"""
		Update the navigation property settings in organization
		
		"""
		tags = ['organization.organizationSettings']

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
		return await self.request_adapter.send_async(request_info, OrganizationSettings, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property settings for organization
		
		"""
		tags = ['organization.organizationSettings']
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



	def with_url(self, raw_url: str) -> SettingsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: SettingsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return SettingsRequest(self.request_adapter, self.path_parameters)

	def contact_insights(self,
		organization_id: str,
	) -> ContactInsightsRequest:
		if organization_id is None:
			raise TypeError("organization_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["organization%2Did"] =  organization_id

		from .contact_insights import ContactInsightsRequest
		return ContactInsightsRequest(self.request_adapter, path_parameters)

	def item_insights(self,
		organization_id: str,
	) -> ItemInsightsRequest:
		if organization_id is None:
			raise TypeError("organization_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["organization%2Did"] =  organization_id

		from .item_insights import ItemInsightsRequest
		return ItemInsightsRequest(self.request_adapter, path_parameters)

	def microsoft_application_data_access(self,
		organization_id: str,
	) -> MicrosoftApplicationDataAccessRequest:
		if organization_id is None:
			raise TypeError("organization_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["organization%2Did"] =  organization_id

		from .microsoft_application_data_access import MicrosoftApplicationDataAccessRequest
		return MicrosoftApplicationDataAccessRequest(self.request_adapter, path_parameters)

	def people_insights(self,
		organization_id: str,
	) -> PeopleInsightsRequest:
		if organization_id is None:
			raise TypeError("organization_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["organization%2Did"] =  organization_id

		from .people_insights import PeopleInsightsRequest
		return PeopleInsightsRequest(self.request_adapter, path_parameters)

