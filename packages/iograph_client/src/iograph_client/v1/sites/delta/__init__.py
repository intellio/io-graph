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
from iograph_models.v1.delta_get_response import DeltaGetResponse


class DeltaRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/sites/delta()", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DeltaGetResponse:
		"""
		Invoke function delta
		Get newly created, updated, or deleted sites without having to perform a full read of the entire sites collection. A delta function call for sites is similar to a GET request, except that by appropriately applying state tokens in one or more of these calls,
you can query for incremental changes in the sites. It allows you to maintain and synchronize a local store of a user's sites without having to fetch all the sites from the server every time.
The application calls the API without specifying any parameters.
The service begins enumerating sites and returns pages of changes to these sites, accompanied by either an @odata.nextLink or an @odata.deltaLink.
Your application should continue making calls using the @odata.nextLink until there's an @odata.deltaLink  in the response. After you receive all the changes, you can apply them to your local state.
To monitor future changes, call the delta API by using the @odata.deltaLink in the previous response. Any resources marked as deleted should be removed from your local state.
		Find more info here: https://learn.microsoft.com/graph/api/site-delta?view=graph-rest-1.0
		"""
		tags = ['sites.site.Functions']

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
		return await self.request_adapter.send_async(request_info, DeltaGetResponse, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def with_url(self, raw_url: str) -> DeltaRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: DeltaRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return DeltaRequest(self.request_adapter, self.path_parameters)

