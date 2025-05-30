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
	from .networkaccess_get_alert_summaries_with_startdatetime_enddatetime import NetworkaccessGetAlertSummariesWithStartDateTimeEndDateTimeRequest
	from .networkaccess_get_alert_severity_summaries_with_startdatetime_enddatetime import NetworkaccessGetAlertSeveritySummariesWithStartDateTimeEndDateTimeRequest
	from .networkaccess_get_alert_frequencies_with_startdatetime_enddatetime import NetworkaccessGetAlertFrequenciesWithStartDateTimeEndDateTimeRequest
	from .count import CountRequest
	from .by_alert_id import ByAlertIdRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.networkaccess_alert_collection_response import NetworkaccessAlertCollectionResponse
from iograph_models.beta.networkaccess_alert import NetworkaccessAlert


class AlertsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/networkAccess/alerts", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> NetworkaccessAlertCollectionResponse:
		"""
		Get alerts from networkAccess
		
		"""
		tags = ['networkAccess.alert']

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
		return await self.request_adapter.send_async(request_info, NetworkaccessAlertCollectionResponse, error_mapping)

	async def post(
		self,
		body: NetworkaccessAlert,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> NetworkaccessAlert:
		"""
		Create new navigation property to alerts for networkAccess
		
		"""
		tags = ['networkAccess.alert']

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
		return await self.request_adapter.send_async(request_info, NetworkaccessAlert, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> AlertsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: AlertsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return AlertsRequest(self.request_adapter, self.path_parameters)

	def by_alert_id(self,
		alert_id: str,
	) -> ByAlertIdRequest:
		if alert_id is None:
			raise TypeError("alert_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["alert%2Did"] =  alert_id

		from .by_alert_id import ByAlertIdRequest
		return ByAlertIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

	def networkaccess_get_alert_frequencies_with_startdatetime_enddatetime(self,
		startDateTime: datetime,
		endDateTime: datetime,
	) -> NetworkaccessGetAlertFrequenciesWithStartDateTimeEndDateTimeRequest:
		if startDateTime is None:
			raise TypeError("startDateTime cannot be null.")
		if endDateTime is None:
			raise TypeError("endDateTime cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["startDateTime"] =  startDateTime
		path_parameters["endDateTime"] =  endDateTime

		from .networkaccess_get_alert_frequencies_with_startdatetime_enddatetime import NetworkaccessGetAlertFrequenciesWithStartDateTimeEndDateTimeRequest
		return NetworkaccessGetAlertFrequenciesWithStartDateTimeEndDateTimeRequest(self.request_adapter, path_parameters)

	def networkaccess_get_alert_severity_summaries_with_startdatetime_enddatetime(self,
		startDateTime: datetime,
		endDateTime: datetime,
	) -> NetworkaccessGetAlertSeveritySummariesWithStartDateTimeEndDateTimeRequest:
		if startDateTime is None:
			raise TypeError("startDateTime cannot be null.")
		if endDateTime is None:
			raise TypeError("endDateTime cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["startDateTime"] =  startDateTime
		path_parameters["endDateTime"] =  endDateTime

		from .networkaccess_get_alert_severity_summaries_with_startdatetime_enddatetime import NetworkaccessGetAlertSeveritySummariesWithStartDateTimeEndDateTimeRequest
		return NetworkaccessGetAlertSeveritySummariesWithStartDateTimeEndDateTimeRequest(self.request_adapter, path_parameters)

	def networkaccess_get_alert_summaries_with_startdatetime_enddatetime(self,
		startDateTime: datetime,
		endDateTime: datetime,
	) -> NetworkaccessGetAlertSummariesWithStartDateTimeEndDateTimeRequest:
		if startDateTime is None:
			raise TypeError("startDateTime cannot be null.")
		if endDateTime is None:
			raise TypeError("endDateTime cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["startDateTime"] =  startDateTime
		path_parameters["endDateTime"] =  endDateTime

		from .networkaccess_get_alert_summaries_with_startdatetime_enddatetime import NetworkaccessGetAlertSummariesWithStartDateTimeEndDateTimeRequest
		return NetworkaccessGetAlertSummariesWithStartDateTimeEndDateTimeRequest(self.request_adapter, path_parameters)

