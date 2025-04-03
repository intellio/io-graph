# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ...request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .by_agreement_id import ByAgreementIdRequest
	from ...request_adapter import HttpxRequestAdapter
from iograph_models.beta.agreement_collection_response import AgreementCollectionResponse
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.agreement import Agreement


class AgreementsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/agreements", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AgreementCollectionResponse:
		"""
		Get entities from agreements
		
		"""
		tags = ['agreements.agreement']

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
		return await self.request_adapter.send_async(request_info, AgreementCollectionResponse, error_mapping)

	async def post(
		self,
		body: Agreement,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Agreement:
		"""
		Add new entity to agreements
		
		"""
		tags = ['agreements.agreement']

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
		return await self.request_adapter.send_async(request_info, Agreement, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> AgreementsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: AgreementsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return AgreementsRequest(self.request_adapter, self.path_parameters)

	def by_agreement_id(self,
		agreement_id: str,
	) -> ByAgreementIdRequest:
		if agreement_id is None:
			raise TypeError("agreement_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["agreement%2Did"] =  agreement_id

		from .by_agreement_id import ByAgreementIdRequest
		return ByAgreementIdRequest(self.request_adapter, path_parameters)

