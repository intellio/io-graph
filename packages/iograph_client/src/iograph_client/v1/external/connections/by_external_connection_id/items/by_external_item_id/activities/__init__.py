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
	from .by_external_activity_id import ByExternalActivityIdRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.v1.external_connectors_external_activity_collection_response import ExternalConnectorsExternalActivityCollectionResponse
from iograph_models.v1.external_connectors_external_activity import ExternalConnectorsExternalActivity
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class ActivitiesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/external/connections/{externalConnection%2Did}/items/{externalItem%2Did}/activities", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ExternalConnectorsExternalActivityCollectionResponse:
		"""
		Get activities from external
		Returns a list of activities performed on the item. Write-only.
		"""
		tags = ['external.externalConnection']

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
		return await self.request_adapter.send_async(request_info, ExternalConnectorsExternalActivityCollectionResponse, error_mapping)

	async def post(
		self,
		body: ExternalConnectorsExternalActivity,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ExternalConnectorsExternalActivity:
		"""
		Create new navigation property to activities for external
		
		"""
		tags = ['external.externalConnection']

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
		return await self.request_adapter.send_async(request_info, ExternalConnectorsExternalActivity, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> ActivitiesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ActivitiesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ActivitiesRequest(self.request_adapter, self.path_parameters)

	def by_external_activity_id(self,
		externalConnection_id: str,
		externalItem_id: str,
		externalActivity_id: str,
	) -> ByExternalActivityIdRequest:
		if externalConnection_id is None:
			raise TypeError("externalConnection_id cannot be null.")
		if externalItem_id is None:
			raise TypeError("externalItem_id cannot be null.")
		if externalActivity_id is None:
			raise TypeError("externalActivity_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["externalConnection%2Did"] =  externalConnection_id
		path_parameters["externalItem%2Did"] =  externalItem_id
		path_parameters["externalActivity%2Did"] =  externalActivity_id

		from .by_external_activity_id import ByExternalActivityIdRequest
		return ByExternalActivityIdRequest(self.request_adapter, path_parameters)

	def count(self,
		externalConnection_id: str,
		externalItem_id: str,
	) -> CountRequest:
		if externalConnection_id is None:
			raise TypeError("externalConnection_id cannot be null.")
		if externalItem_id is None:
			raise TypeError("externalItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["externalConnection%2Did"] =  externalConnection_id
		path_parameters["externalItem%2Did"] =  externalItem_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

