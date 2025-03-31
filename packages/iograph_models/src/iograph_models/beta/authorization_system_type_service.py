from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from pydantic import BaseModel, Field


class AuthorizationSystemTypeService(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.authorizationSystemTypeService"] = Field(alias="@odata.type",)
	actions: Optional[list[Annotated[Union[AwsAuthorizationSystemTypeAction, AzureAuthorizationSystemTypeAction, GcpAuthorizationSystemTypeAction],Field(discriminator="odata_type")]]] = Field(alias="actions", default=None,)

from .aws_authorization_system_type_action import AwsAuthorizationSystemTypeAction
from .azure_authorization_system_type_action import AzureAuthorizationSystemTypeAction
from .gcp_authorization_system_type_action import GcpAuthorizationSystemTypeAction
