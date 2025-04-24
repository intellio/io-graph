from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .request_information import RequestInformation
from .request_adapter import ModelType
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


if TYPE_CHECKING:
    from .request_adapter import HttpxRequestAdapter


class RawRequest(BaseRequestBuilder):
	def __init__(
		self,
		request_adapter: HttpxRequestAdapter,
		path_parameters: Optional[Union[dict[str, Any], str]],
		endpoint_str: str,
		return_model: ModelType | None,
	) -> None:

		super().__init__(request_adapter, "{+baseurl}" + endpoint_str, path_parameters)
		self.return_model = return_model

	async def get(self, request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,) -> ModelType | str | None:

		error_mapping: dict[str, type[BaseModel]] = {"XXX": ODataErrorsODataError,}

		request_info: RequestInformation = RequestInformation(
			method = Method.GET,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		return await self.request_adapter.send_async(request_info, self.return_model, error_mapping)

	async def post(
		self,
		body: ModelType | str,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ModelType | str | None:
		
		error_mapping: dict[str, type[BaseModel]] = {"XXX": ODataErrorsODataError,}

		request_info: RequestInformation = RequestInformation(
			method = Method.POST,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		request_info.set_content(body, "application/json")
		return await self.request_adapter.send_async(request_info, self.return_model, error_mapping)

	async def patch(
		self,
		body: ModelType | str,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ModelType | str | None:
		
		error_mapping: dict[str, type[BaseModel]] = {"XXX": ODataErrorsODataError,}

		request_info: RequestInformation = RequestInformation(
			method = Method.PATCH,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		request_info.set_content(body, "application/json")
		return await self.request_adapter.send_async(request_info, self.return_model, error_mapping)
	
	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")
