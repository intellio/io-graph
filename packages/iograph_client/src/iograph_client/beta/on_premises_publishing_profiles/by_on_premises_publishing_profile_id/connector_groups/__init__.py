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
	from .count import CountRequest
	from .by_connector_group_id import ByConnectorGroupIdRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.connector_group import ConnectorGroup
from iograph_models.beta.connector_group_collection_response import ConnectorGroupCollectionResponse
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ConnectorGroupsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/onPremisesPublishingProfiles/{onPremisesPublishingProfile%2Did}/connectorGroups", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ConnectorGroupCollectionResponse:
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
		return await self.request_adapter.send_async(request_info, ConnectorGroupCollectionResponse, error_mapping)

	async def post(
		self,
		body: ConnectorGroup,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ConnectorGroup:
		"""
		Create new navigation property to connectorGroups for onPremisesPublishingProfiles
		
		"""
		tags = ['onPremisesPublishingProfiles.connectorGroup']

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
		return await self.request_adapter.send_async(request_info, ConnectorGroup, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> ConnectorGroupsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ConnectorGroupsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ConnectorGroupsRequest(self.request_adapter, self.path_parameters)

	def by_connector_group_id(self,
		onPremisesPublishingProfile_id: str,
		connectorGroup_id: str,
	) -> ByConnectorGroupIdRequest:
		if onPremisesPublishingProfile_id is None:
			raise TypeError("onPremisesPublishingProfile_id cannot be null.")
		if connectorGroup_id is None:
			raise TypeError("connectorGroup_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["onPremisesPublishingProfile%2Did"] =  onPremisesPublishingProfile_id
		path_parameters["connectorGroup%2Did"] =  connectorGroup_id

		from .by_connector_group_id import ByConnectorGroupIdRequest
		return ByConnectorGroupIdRequest(self.request_adapter, path_parameters)

	def count(self,
		onPremisesPublishingProfile_id: str,
	) -> CountRequest:
		if onPremisesPublishingProfile_id is None:
			raise TypeError("onPremisesPublishingProfile_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["onPremisesPublishingProfile%2Did"] =  onPremisesPublishingProfile_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

