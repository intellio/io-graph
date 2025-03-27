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
	from .by_detection_rule_id import ByDetectionRuleIdRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.security_detection_rule import SecurityDetectionRule
from iograph_models.beta.security_detection_rule_collection_response import SecurityDetectionRuleCollectionResponse
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class DetectionRulesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/security/rules/detectionRules", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SecurityDetectionRuleCollectionResponse:
		"""
		List detectionRules
		Get a list of custom detection rules.
With custom detections, you can proactively monitor for and respond to various events and system states, including suspected breach activity and misconfigured assets in their organization network.
Custom detection rules, which are written in Kusto query language (KQL), automatically trigger alerts and response actions once there are events matching their KQL queries.
		Find more info here: https://learn.microsoft.com/graph/api/security-detectionrule-list?view=graph-rest-beta
		"""
		tags = ['security.rulesRoot']

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
		return await self.request_adapter.send_async(request_info, SecurityDetectionRuleCollectionResponse, error_mapping)

	async def post(
		self,
		body: SecurityDetectionRule,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> SecurityDetectionRule:
		"""
		Create new navigation property to detectionRules for security
		
		"""
		tags = ['security.rulesRoot']

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
		return await self.request_adapter.send_async(request_info, SecurityDetectionRule, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> DetectionRulesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: DetectionRulesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return DetectionRulesRequest(self.request_adapter, self.path_parameters)

	def by_detection_rule_id(self,
		detectionRule_id: str,
	) -> ByDetectionRuleIdRequest:
		if detectionRule_id is None:
			raise TypeError("detectionRule_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["detectionRule%2Did"] =  detectionRule_id

		from .by_detection_rule_id import ByDetectionRuleIdRequest
		return ByDetectionRuleIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

