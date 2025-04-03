from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from pydantic import BaseModel, Field


class PrivilegeEscalation(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.privilegeEscalation"] = Field(alias="@odata.type", default="#microsoft.graph.privilegeEscalation")
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	actions: Optional[list[Annotated[Union[AwsAuthorizationSystemTypeAction, AzureAuthorizationSystemTypeAction, GcpAuthorizationSystemTypeAction],Field(discriminator="odata_type")]]] = Field(alias="actions", default=None,)
	resources: Optional[list[Annotated[Union[AwsAuthorizationSystemResource, AzureAuthorizationSystemResource, GcpAuthorizationSystemResource],Field(discriminator="odata_type")]]] = Field(alias="resources", default=None,)

from .aws_authorization_system_type_action import AwsAuthorizationSystemTypeAction
from .azure_authorization_system_type_action import AzureAuthorizationSystemTypeAction
from .gcp_authorization_system_type_action import GcpAuthorizationSystemTypeAction
from .aws_authorization_system_resource import AwsAuthorizationSystemResource
from .azure_authorization_system_resource import AzureAuthorizationSystemResource
from .gcp_authorization_system_resource import GcpAuthorizationSystemResource
