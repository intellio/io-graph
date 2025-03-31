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
	from .ediscovery_update_index import EdiscoveryUpdateIndexRequest
	from .ediscovery_remove_hold import EdiscoveryRemoveHoldRequest
	from .ediscovery_release import EdiscoveryReleaseRequest
	from .ediscovery_apply_hold import EdiscoveryApplyHoldRequest
	from .ediscovery_activate import EdiscoveryActivateRequest
	from .last_index_operation import LastIndexOperationRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.beta.ediscovery_custodian import EdiscoveryCustodian
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByCustodianIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/compliance/ediscovery/cases/{case%2Did}/custodians/{custodian%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> EdiscoveryCustodian:
		"""
		Get custodian
		Read the properties and relationships of a custodian object.
		Find more info here: https://learn.microsoft.com/graph/api/ediscovery-custodian-get?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, EdiscoveryCustodian, error_mapping)

	async def patch(
		self,
		body: EdiscoveryCustodian,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> EdiscoveryCustodian:
		"""
		Update custodian
		Update the properties of a custodian object.
		Find more info here: https://learn.microsoft.com/graph/api/ediscovery-custodian-update?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, EdiscoveryCustodian, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property custodians for compliance
		
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



	def with_url(self, raw_url: str) -> ByCustodianIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByCustodianIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByCustodianIdRequest(self.request_adapter, self.path_parameters)

	def last_index_operation(self,
		case_id: str,
		custodian_id: str,
	) -> LastIndexOperationRequest:
		if case_id is None:
			raise TypeError("case_id cannot be null.")
		if custodian_id is None:
			raise TypeError("custodian_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["case%2Did"] =  case_id
		path_parameters["custodian%2Did"] =  custodian_id

		from .last_index_operation import LastIndexOperationRequest
		return LastIndexOperationRequest(self.request_adapter, path_parameters)

	def ediscovery_activate(self,
		case_id: str,
		custodian_id: str,
	) -> EdiscoveryActivateRequest:
		if case_id is None:
			raise TypeError("case_id cannot be null.")
		if custodian_id is None:
			raise TypeError("custodian_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["case%2Did"] =  case_id
		path_parameters["custodian%2Did"] =  custodian_id

		from .ediscovery_activate import EdiscoveryActivateRequest
		return EdiscoveryActivateRequest(self.request_adapter, path_parameters)

	def ediscovery_apply_hold(self,
		case_id: str,
		custodian_id: str,
	) -> EdiscoveryApplyHoldRequest:
		if case_id is None:
			raise TypeError("case_id cannot be null.")
		if custodian_id is None:
			raise TypeError("custodian_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["case%2Did"] =  case_id
		path_parameters["custodian%2Did"] =  custodian_id

		from .ediscovery_apply_hold import EdiscoveryApplyHoldRequest
		return EdiscoveryApplyHoldRequest(self.request_adapter, path_parameters)

	def ediscovery_release(self,
		case_id: str,
		custodian_id: str,
	) -> EdiscoveryReleaseRequest:
		if case_id is None:
			raise TypeError("case_id cannot be null.")
		if custodian_id is None:
			raise TypeError("custodian_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["case%2Did"] =  case_id
		path_parameters["custodian%2Did"] =  custodian_id

		from .ediscovery_release import EdiscoveryReleaseRequest
		return EdiscoveryReleaseRequest(self.request_adapter, path_parameters)

	def ediscovery_remove_hold(self,
		case_id: str,
		custodian_id: str,
	) -> EdiscoveryRemoveHoldRequest:
		if case_id is None:
			raise TypeError("case_id cannot be null.")
		if custodian_id is None:
			raise TypeError("custodian_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["case%2Did"] =  case_id
		path_parameters["custodian%2Did"] =  custodian_id

		from .ediscovery_remove_hold import EdiscoveryRemoveHoldRequest
		return EdiscoveryRemoveHoldRequest(self.request_adapter, path_parameters)

	def ediscovery_update_index(self,
		case_id: str,
		custodian_id: str,
	) -> EdiscoveryUpdateIndexRequest:
		if case_id is None:
			raise TypeError("case_id cannot be null.")
		if custodian_id is None:
			raise TypeError("custodian_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["case%2Did"] =  case_id
		path_parameters["custodian%2Did"] =  custodian_id

		from .ediscovery_update_index import EdiscoveryUpdateIndexRequest
		return EdiscoveryUpdateIndexRequest(self.request_adapter, path_parameters)

	def site_sources(self,
		case_id: str,
		custodian_id: str,
	) -> SiteSourcesRequest:
		if case_id is None:
			raise TypeError("case_id cannot be null.")
		if custodian_id is None:
			raise TypeError("custodian_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["case%2Did"] =  case_id
		path_parameters["custodian%2Did"] =  custodian_id

		from .site_sources import SiteSourcesRequest
		return SiteSourcesRequest(self.request_adapter, path_parameters)

	def unified_group_sources(self,
		case_id: str,
		custodian_id: str,
	) -> UnifiedGroupSourcesRequest:
		if case_id is None:
			raise TypeError("case_id cannot be null.")
		if custodian_id is None:
			raise TypeError("custodian_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["case%2Did"] =  case_id
		path_parameters["custodian%2Did"] =  custodian_id

		from .unified_group_sources import UnifiedGroupSourcesRequest
		return UnifiedGroupSourcesRequest(self.request_adapter, path_parameters)

	def user_sources(self,
		case_id: str,
		custodian_id: str,
	) -> UserSourcesRequest:
		if case_id is None:
			raise TypeError("case_id cannot be null.")
		if custodian_id is None:
			raise TypeError("custodian_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["case%2Did"] =  case_id
		path_parameters["custodian%2Did"] =  custodian_id

		from .user_sources import UserSourcesRequest
		return UserSourcesRequest(self.request_adapter, path_parameters)

