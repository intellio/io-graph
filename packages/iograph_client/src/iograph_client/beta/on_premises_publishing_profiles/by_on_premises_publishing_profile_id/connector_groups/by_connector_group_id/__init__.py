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
	from .members import MembersRequest
	from .applications_with_uniquename import ApplicationsWithUniqueNameRequest
	from .applications_with_appid import ApplicationsWithAppIdRequest
	from .applications import ApplicationsRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.connector_group import ConnectorGroup


class ByConnectorGroupIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/onPremisesPublishingProfiles/{onPremisesPublishingProfile%2Did}/connectorGroups/{connectorGroup%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ConnectorGroup:
		"""
		Get connectorGroups from onPremisesPublishingProfiles
		List of existing connectorGroup objects for applications published through Application Proxy. Read-only. Nullable.
		"""
		tags = ['onPremisesPublishingProfiles.connectorGroup']

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
		return await self.request_adapter.send_async(request_info, ConnectorGroup, error_mapping)

	async def patch(
		self,
		body: ConnectorGroup,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ConnectorGroup:
		"""
		Update the navigation property connectorGroups in onPremisesPublishingProfiles
		
		"""
		tags = ['onPremisesPublishingProfiles.connectorGroup']

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
		return await self.request_adapter.send_async(request_info, ConnectorGroup, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property connectorGroups for onPremisesPublishingProfiles
		
		"""
		tags = ['onPremisesPublishingProfiles.connectorGroup']
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



	def with_url(self, raw_url: str) -> ByConnectorGroupIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByConnectorGroupIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByConnectorGroupIdRequest(self.request_adapter, self.path_parameters)

	def applications(self,
		onPremisesPublishingProfile_id: str,
		connectorGroup_id: str,
	) -> ApplicationsRequest:
		if onPremisesPublishingProfile_id is None:
			raise TypeError("onPremisesPublishingProfile_id cannot be null.")
		if connectorGroup_id is None:
			raise TypeError("connectorGroup_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["onPremisesPublishingProfile%2Did"] =  onPremisesPublishingProfile_id
		path_parameters["connectorGroup%2Did"] =  connectorGroup_id

		from .applications import ApplicationsRequest
		return ApplicationsRequest(self.request_adapter, path_parameters)

	def applications_with_appid(self,
		onPremisesPublishingProfile_id: str,
		connectorGroup_id: str,
		appId: str,
	) -> ApplicationsWithAppIdRequest:
		if onPremisesPublishingProfile_id is None:
			raise TypeError("onPremisesPublishingProfile_id cannot be null.")
		if connectorGroup_id is None:
			raise TypeError("connectorGroup_id cannot be null.")
		if appId is None:
			raise TypeError("appId cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["onPremisesPublishingProfile%2Did"] =  onPremisesPublishingProfile_id
		path_parameters["connectorGroup%2Did"] =  connectorGroup_id
		path_parameters["appId"] =  appId

		from .applications_with_appid import ApplicationsWithAppIdRequest
		return ApplicationsWithAppIdRequest(self.request_adapter, path_parameters)

	def applications_with_uniquename(self,
		onPremisesPublishingProfile_id: str,
		connectorGroup_id: str,
		uniqueName: str,
	) -> ApplicationsWithUniqueNameRequest:
		if onPremisesPublishingProfile_id is None:
			raise TypeError("onPremisesPublishingProfile_id cannot be null.")
		if connectorGroup_id is None:
			raise TypeError("connectorGroup_id cannot be null.")
		if uniqueName is None:
			raise TypeError("uniqueName cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["onPremisesPublishingProfile%2Did"] =  onPremisesPublishingProfile_id
		path_parameters["connectorGroup%2Did"] =  connectorGroup_id
		path_parameters["uniqueName"] =  uniqueName

		from .applications_with_uniquename import ApplicationsWithUniqueNameRequest
		return ApplicationsWithUniqueNameRequest(self.request_adapter, path_parameters)

	def members(self,
		onPremisesPublishingProfile_id: str,
		connectorGroup_id: str,
	) -> MembersRequest:
		if onPremisesPublishingProfile_id is None:
			raise TypeError("onPremisesPublishingProfile_id cannot be null.")
		if connectorGroup_id is None:
			raise TypeError("connectorGroup_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["onPremisesPublishingProfile%2Did"] =  onPremisesPublishingProfile_id
		path_parameters["connectorGroup%2Did"] =  connectorGroup_id

		from .members import MembersRequest
		return MembersRequest(self.request_adapter, path_parameters)

