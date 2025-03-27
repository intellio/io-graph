from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityDiscoveredCloudAppDetail(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	category: Optional[SecurityAppCategory | str] = Field(alias="category", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	domains: Optional[list[str]] = Field(alias="domains", default=None,)
	downloadNetworkTrafficInBytes: Optional[int] = Field(alias="downloadNetworkTrafficInBytes", default=None,)
	firstSeenDateTime: Optional[datetime] = Field(alias="firstSeenDateTime", default=None,)
	ipAddressCount: Optional[int] = Field(alias="ipAddressCount", default=None,)
	lastSeenDateTime: Optional[datetime] = Field(alias="lastSeenDateTime", default=None,)
	riskScore: Optional[int] = Field(alias="riskScore", default=None,)
	tags: Optional[list[str]] = Field(alias="tags", default=None,)
	transactionCount: Optional[int] = Field(alias="transactionCount", default=None,)
	uploadNetworkTrafficInBytes: Optional[int] = Field(alias="uploadNetworkTrafficInBytes", default=None,)
	userCount: Optional[int] = Field(alias="userCount", default=None,)
	appInfo: Optional[SecurityDiscoveredCloudAppInfo] = Field(alias="appInfo", default=None,)
	ipAddresses: Optional[list[SecurityDiscoveredCloudAppIPAddress]] = Field(alias="ipAddresses", default=None,)
	users: Optional[list[SecurityDiscoveredCloudAppUser]] = Field(alias="users", default=None,)

	@model_validator(mode="wrap")
	def convert_discriminator_class(cls, data: Any, handler: ModelWrapValidatorHandler[Self]) -> Self:
		try:
			# check with parent model to catch any errors
			parent_validated_model = handler(data)
			# check if the discriminator field is present
			if "@odata.type" not in data:
				return parent_validated_model
			# get the discriminator value
			mapping_key = data["@odata.type"]
			if mapping_key == "#microsoft.graph.security.endpointDiscoveredCloudAppDetail":
				from .security_endpoint_discovered_cloud_app_detail import SecurityEndpointDiscoveredCloudAppDetail
				return SecurityEndpointDiscoveredCloudAppDetail.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .security_app_category import SecurityAppCategory
from .security_discovered_cloud_app_info import SecurityDiscoveredCloudAppInfo
from .security_discovered_cloud_app_i_p_address import SecurityDiscoveredCloudAppIPAddress
from .security_discovered_cloud_app_user import SecurityDiscoveredCloudAppUser

