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
	from .count import CountRequest
	from .by_risky_service_principal_history_item_id import ByRiskyServicePrincipalHistoryItemIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.risky_service_principal_history_item import RiskyServicePrincipalHistoryItem
from iograph_models.beta.risky_service_principal_history_item_collection_response import RiskyServicePrincipalHistoryItemCollectionResponse
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class HistoryRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identityProtection/riskyServicePrincipals/{riskyServicePrincipal%2Did}/history", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> RiskyServicePrincipalHistoryItemCollectionResponse:
		"""
		List history (risk history of riskyServicePrincipal)
		Get the risk history of a riskyServicePrincipal object.
		Find more info here: https://learn.microsoft.com/graph/api/riskyserviceprincipal-list-history?view=graph-rest-beta
		"""
		tags = ['identityProtection.riskyServicePrincipal']

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
		return await self.request_adapter.send_async(request_info, RiskyServicePrincipalHistoryItemCollectionResponse, error_mapping)

	async def post(
		self,
		body: RiskyServicePrincipalHistoryItem,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> RiskyServicePrincipalHistoryItem:
		"""
		Create new navigation property to history for identityProtection
		
		"""
		tags = ['identityProtection.riskyServicePrincipal']

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
		return await self.request_adapter.send_async(request_info, RiskyServicePrincipalHistoryItem, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> HistoryRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: HistoryRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return HistoryRequest(self.request_adapter, self.path_parameters)

	def by_risky_service_principal_history_item_id(self,
		riskyServicePrincipal_id: str,
		riskyServicePrincipalHistoryItem_id: str,
	) -> ByRiskyServicePrincipalHistoryItemIdRequest:
		if riskyServicePrincipal_id is None:
			raise TypeError("riskyServicePrincipal_id cannot be null.")
		if riskyServicePrincipalHistoryItem_id is None:
			raise TypeError("riskyServicePrincipalHistoryItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["riskyServicePrincipal%2Did"] =  riskyServicePrincipal_id
		path_parameters["riskyServicePrincipalHistoryItem%2Did"] =  riskyServicePrincipalHistoryItem_id

		from .by_risky_service_principal_history_item_id import ByRiskyServicePrincipalHistoryItemIdRequest
		return ByRiskyServicePrincipalHistoryItemIdRequest(self.request_adapter, path_parameters)

	def count(self,
		riskyServicePrincipal_id: str,
	) -> CountRequest:
		if riskyServicePrincipal_id is None:
			raise TypeError("riskyServicePrincipal_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["riskyServicePrincipal%2Did"] =  riskyServicePrincipal_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

