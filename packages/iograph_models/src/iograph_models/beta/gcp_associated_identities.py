from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class GcpAssociatedIdentities(BaseModel):
	all: Optional[list[Annotated[Union[GcpCloudFunction, GcpGroup, GcpServiceAccount, GcpUser],Field(discriminator="odata_type")]]] = Field(alias="all", default=None,)
	serviceAccounts: Optional[list[GcpServiceAccount]] = Field(alias="serviceAccounts", default=None,)
	users: Optional[list[GcpUser]] = Field(alias="users", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .gcp_cloud_function import GcpCloudFunction
from .gcp_group import GcpGroup
from .gcp_service_account import GcpServiceAccount
from .gcp_user import GcpUser
from .gcp_service_account import GcpServiceAccount
from .gcp_user import GcpUser

