# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.models.security_run_hunting_query_post_request import Security_run_hunting_queryPostRequest
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.security_hunting_query_results import SecurityHuntingQueryResults


class SecurityRunHuntingQueryRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/security/microsoft.graph.security.runHuntingQuery"
		self.path_parameters: dict[str, Any] = path_parameters

	async def post(
		self,
		body: Security_run_hunting_queryPostRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> SecurityHuntingQueryResults:
		"""
		Invoke action runHuntingQuery
		Queries a specified set of event, activity, or entity data supported by Microsoft 365 Defender to proactively look for specific threats in your environment. This method is for advanced hunting in Microsoft 365 Defender. This method includes a query in Kusto Query Language (KQL). It specifies a data table in the advanced hunting schema and a piped sequence of operators to filter or search that data, and format the query output in specific ways.  Find out more about hunting for threats across devices, emails, apps, and identities. Learn about KQL. For information on using advanced hunting in the Microsoft 365 Defender portal, see Proactively hunt for threats with advanced hunting in Microsoft 365 Defender.
		"""
		tags = ['security.security.Actions']

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
		return await self.request_adapter.send_async(request_info, SecurityHuntingQueryResults, error_mapping)


