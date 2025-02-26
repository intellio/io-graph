# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_delegated_permission_classification_id import ByDelegatedPermissionClassificationIdRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.models.delegated_permission_classification_collection_response import DelegatedPermissionClassificationCollectionResponse
from iograph_models.models.delegated_permission_classification import DelegatedPermissionClassification
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class DelegatedPermissionClassificationsRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/servicePrincipals/{servicePrincipal%2Did}/delegatedPermissionClassifications"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DelegatedPermissionClassificationCollectionResponse:
		"""
		List delegatedPermissionClassifications collection of servicePrincipal
		Retrieve the list of delegatedPermissionClassification currently configured for the delegated permissions exposed by an API.
		Find more info here: https://learn.microsoft.com/graph/api/serviceprincipal-list-delegatedpermissionclassifications?view=graph-rest-1.0
		"""
		tags = ['servicePrincipals.delegatedPermissionClassification']

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
		return await self.request_adapter.send_async(request_info, DelegatedPermissionClassificationCollectionResponse, error_mapping)

	async def post(
		self,
		body: DelegatedPermissionClassification,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> DelegatedPermissionClassification:
		"""
		Create delegatedPermissionClassification
		Classify a delegated permission by adding a delegatedPermissionClassification to the servicePrincipal representing the API.
		Find more info here: https://learn.microsoft.com/graph/api/serviceprincipal-post-delegatedpermissionclassifications?view=graph-rest-1.0
		"""
		tags = ['servicePrincipals.delegatedPermissionClassification']

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
		return await self.request_adapter.send_async(request_info, DelegatedPermissionClassification, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def by_delegated_permission_classification_id(self,
		servicePrincipal_id: str,
		delegatedPermissionClassification_id: str,
	) -> ByDelegatedPermissionClassificationIdRequest:
		if servicePrincipal_id is None:
			raise TypeError("servicePrincipal_id cannot be null.")
		if delegatedPermissionClassification_id is None:
			raise TypeError("delegatedPermissionClassification_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["servicePrincipal%2Did"] =  servicePrincipal_id
		path_parameters["delegatedPermissionClassification%2Did"] =  delegatedPermissionClassification_id

		from .by_delegated_permission_classification_id import ByDelegatedPermissionClassificationIdRequest
		return ByDelegatedPermissionClassificationIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

