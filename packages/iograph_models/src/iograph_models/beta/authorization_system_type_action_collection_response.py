from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class AuthorizationSystemTypeActionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[AwsAuthorizationSystemTypeAction, AzureAuthorizationSystemTypeAction, GcpAuthorizationSystemTypeAction],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .aws_authorization_system_type_action import AwsAuthorizationSystemTypeAction
from .azure_authorization_system_type_action import AzureAuthorizationSystemTypeAction
from .gcp_authorization_system_type_action import GcpAuthorizationSystemTypeAction

