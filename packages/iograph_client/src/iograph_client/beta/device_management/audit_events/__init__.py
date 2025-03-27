# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .get_audit_categories import GetAuditCategoriesRequest
	from .get_audit_activity_types_with_category import GetAuditActivityTypesWithCategoryRequest
	from .count import CountRequest
	from .by_audit_event_id import ByAuditEventIdRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.audit_event_collection_response import AuditEventCollectionResponse
from iograph_models.beta.audit_event import AuditEvent


class AuditEventsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/auditEvents", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AuditEventCollectionResponse:
		"""
		Get auditEvents from deviceManagement
		The Audit Events
		"""
		tags = ['deviceManagement.auditEvent']

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
		return await self.request_adapter.send_async(request_info, AuditEventCollectionResponse, error_mapping)

	async def post(
		self,
		body: AuditEvent,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> AuditEvent:
		"""
		Create new navigation property to auditEvents for deviceManagement
		
		"""
		tags = ['deviceManagement.auditEvent']

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
		return await self.request_adapter.send_async(request_info, AuditEvent, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> AuditEventsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: AuditEventsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return AuditEventsRequest(self.request_adapter, self.path_parameters)

	def by_audit_event_id(self,
		auditEvent_id: str,
	) -> ByAuditEventIdRequest:
		if auditEvent_id is None:
			raise TypeError("auditEvent_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["auditEvent%2Did"] =  auditEvent_id

		from .by_audit_event_id import ByAuditEventIdRequest
		return ByAuditEventIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

	def get_audit_activity_types_with_category(self,
		category: str,
	) -> GetAuditActivityTypesWithCategoryRequest:
		if category is None:
			raise TypeError("category cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["category"] =  category

		from .get_audit_activity_types_with_category import GetAuditActivityTypesWithCategoryRequest
		return GetAuditActivityTypesWithCategoryRequest(self.request_adapter, path_parameters)

	@property
	def get_audit_categories(self,
	) -> GetAuditCategoriesRequest:
		from .get_audit_categories import GetAuditCategoriesRequest
		return GetAuditCategoriesRequest(self.request_adapter, self.path_parameters)

