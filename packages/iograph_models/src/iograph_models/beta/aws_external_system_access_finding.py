from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class AwsExternalSystemAccessFinding(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.awsExternalSystemAccessFinding"] = Field(alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	accessMethods: Optional[ExternalSystemAccessMethods | str] = Field(alias="accessMethods", default=None,)
	systemWithAccess: Optional[AuthorizationSystemInfo] = Field(alias="systemWithAccess", default=None,)
	trustedIdentityCount: Optional[int] = Field(alias="trustedIdentityCount", default=None,)
	trustsAllIdentities: Optional[bool] = Field(alias="trustsAllIdentities", default=None,)
	affectedSystem: Optional[Union[AwsAuthorizationSystem, AzureAuthorizationSystem, GcpAuthorizationSystem]] = Field(alias="affectedSystem", default=None,discriminator="odata_type", )

from .external_system_access_methods import ExternalSystemAccessMethods
from .authorization_system_info import AuthorizationSystemInfo
from .aws_authorization_system import AwsAuthorizationSystem
from .azure_authorization_system import AzureAuthorizationSystem
from .gcp_authorization_system import GcpAuthorizationSystem
