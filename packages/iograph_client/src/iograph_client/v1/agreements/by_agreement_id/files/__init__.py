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
	from .by_agreement_file_localization_id import ByAgreementFileLocalizationIdRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.v1.agreement_file_localization_collection_response import AgreementFileLocalizationCollectionResponse
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.v1.agreement_file_localization import AgreementFileLocalization


class FilesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/agreements/{agreement%2Did}/files", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AgreementFileLocalizationCollectionResponse:
		"""
		Get files from agreements
		PDFs linked to this agreement. This property is in the process of being deprecated. Use the  file property instead. Supports $expand.
		"""
		tags = ['agreements.agreementFileLocalization']

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
		return await self.request_adapter.send_async(request_info, AgreementFileLocalizationCollectionResponse, error_mapping)

	async def post(
		self,
		body: AgreementFileLocalization,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> AgreementFileLocalization:
		"""
		Create new navigation property to files for agreements
		
		"""
		tags = ['agreements.agreementFileLocalization']

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
		return await self.request_adapter.send_async(request_info, AgreementFileLocalization, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> FilesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: FilesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return FilesRequest(self.request_adapter, self.path_parameters)

	def by_agreement_file_localization_id(self,
		agreement_id: str,
		agreementFileLocalization_id: str,
	) -> ByAgreementFileLocalizationIdRequest:
		if agreement_id is None:
			raise TypeError("agreement_id cannot be null.")
		if agreementFileLocalization_id is None:
			raise TypeError("agreementFileLocalization_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["agreement%2Did"] =  agreement_id
		path_parameters["agreementFileLocalization%2Did"] =  agreementFileLocalization_id

		from .by_agreement_file_localization_id import ByAgreementFileLocalizationIdRequest
		return ByAgreementFileLocalizationIdRequest(self.request_adapter, path_parameters)

	def count(self,
		agreement_id: str,
	) -> CountRequest:
		if agreement_id is None:
			raise TypeError("agreement_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["agreement%2Did"] =  agreement_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

