# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .files import FilesRequest
	from .file import FileRequest
	from .acceptances import AcceptancesRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.agreement import Agreement


class ByAgreementIdRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/identityGovernance/termsOfUse/agreements/{agreement%2Did}"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Agreement:
		"""
		List files (terms of use agreement files)
		Retrieve all files related to an agreement. This includes the default file and all localized files.
		Find more info here: https://learn.microsoft.com/graph/api/agreement-list-files?view=graph-rest-1.0
		"""
		tags = ['identityGovernance.termsOfUseContainer']

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
		return await self.request_adapter.send_async(request_info, Agreement, error_mapping)

	async def patch(
		self,
		body: Agreement,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Agreement:
		"""
		Update agreement
		Update the properties of an agreement object.
		Find more info here: https://learn.microsoft.com/graph/api/agreement-update?view=graph-rest-1.0
		"""
		tags = ['identityGovernance.termsOfUseContainer']

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
		return await self.request_adapter.send_async(request_info, Agreement, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete agreement
		Delete an agreement object.
		Find more info here: https://learn.microsoft.com/graph/api/agreement-delete?view=graph-rest-1.0
		"""
		tags = ['identityGovernance.termsOfUseContainer']
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



	@property
	def acceptances(self,
	) -> AcceptancesRequest:
		from .acceptances import AcceptancesRequest
		return AcceptancesRequest(self.request_adapter, self.path_parameters)

	@property
	def file(self,
	) -> FileRequest:
		from .file import FileRequest
		return FileRequest(self.request_adapter, self.path_parameters)

	@property
	def files(self,
	) -> FilesRequest:
		from .files import FilesRequest
		return FilesRequest(self.request_adapter, self.path_parameters)

