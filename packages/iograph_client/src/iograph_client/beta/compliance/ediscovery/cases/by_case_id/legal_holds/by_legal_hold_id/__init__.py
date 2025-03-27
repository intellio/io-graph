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
	from .user_sources import UserSourcesRequest
	from .unified_group_sources import UnifiedGroupSourcesRequest
	from .site_sources import SiteSourcesRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.ediscovery_legal_hold import EdiscoveryLegalHold


class ByLegalHoldIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/compliance/ediscovery/cases/{case%2Did}/legalHolds/{legalHold%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> EdiscoveryLegalHold:
		"""
		Get legalHold
		Read the properties and relationships of a legalHold object.
		Find more info here: https://learn.microsoft.com/graph/api/ediscovery-legalhold-get?view=graph-rest-beta
		"""
		tags = ['compliance.ediscoveryroot']

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
		return await self.request_adapter.send_async(request_info, EdiscoveryLegalHold, error_mapping)

	async def patch(
		self,
		body: EdiscoveryLegalHold,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> EdiscoveryLegalHold:
		"""
		Update legalHold
		Update the properties of a legalHold object.
		Find more info here: https://learn.microsoft.com/graph/api/ediscovery-legalhold-update?view=graph-rest-beta
		"""
		tags = ['compliance.ediscoveryroot']

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
		return await self.request_adapter.send_async(request_info, EdiscoveryLegalHold, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete legalHold
		Delete a legalHold object.
		Find more info here: https://learn.microsoft.com/graph/api/ediscovery-legalhold-delete?view=graph-rest-beta
		"""
		tags = ['compliance.ediscoveryroot']
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



	def with_url(self, raw_url: str) -> ByLegalHoldIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByLegalHoldIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByLegalHoldIdRequest(self.request_adapter, self.path_parameters)

	def site_sources(self,
		case_id: str,
		legalHold_id: str,
	) -> SiteSourcesRequest:
		if case_id is None:
			raise TypeError("case_id cannot be null.")
		if legalHold_id is None:
			raise TypeError("legalHold_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["case%2Did"] =  case_id
		path_parameters["legalHold%2Did"] =  legalHold_id

		from .site_sources import SiteSourcesRequest
		return SiteSourcesRequest(self.request_adapter, path_parameters)

	def unified_group_sources(self,
		case_id: str,
		legalHold_id: str,
	) -> UnifiedGroupSourcesRequest:
		if case_id is None:
			raise TypeError("case_id cannot be null.")
		if legalHold_id is None:
			raise TypeError("legalHold_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["case%2Did"] =  case_id
		path_parameters["legalHold%2Did"] =  legalHold_id

		from .unified_group_sources import UnifiedGroupSourcesRequest
		return UnifiedGroupSourcesRequest(self.request_adapter, path_parameters)

	def user_sources(self,
		case_id: str,
		legalHold_id: str,
	) -> UserSourcesRequest:
		if case_id is None:
			raise TypeError("case_id cannot be null.")
		if legalHold_id is None:
			raise TypeError("legalHold_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["case%2Did"] =  case_id
		path_parameters["legalHold%2Did"] =  legalHold_id

		from .user_sources import UserSourcesRequest
		return UserSourcesRequest(self.request_adapter, path_parameters)

