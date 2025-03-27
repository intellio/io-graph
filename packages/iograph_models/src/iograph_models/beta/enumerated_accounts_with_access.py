from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class EnumeratedAccountsWithAccess(BaseModel):
	odata_type: Literal["#microsoft.graph.enumeratedAccountsWithAccess"] = Field(alias="@odata.type", default="#microsoft.graph.enumeratedAccountsWithAccess")
	accounts: Optional[list[Annotated[Union[AwsAuthorizationSystem, AzureAuthorizationSystem, GcpAuthorizationSystem],Field(discriminator="odata_type")]]] = Field(alias="accounts", default=None,)

from .aws_authorization_system import AwsAuthorizationSystem
from .azure_authorization_system import AzureAuthorizationSystem
from .gcp_authorization_system import GcpAuthorizationSystem

