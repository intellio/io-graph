from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class GcpAssociatedIdentities(BaseModel):
	all: SerializeAsAny[Optional[list[GcpIdentity]]] = Field(alias="all",default=None,)
	serviceAccounts: Optional[list[GcpServiceAccount]] = Field(alias="serviceAccounts",default=None,)
	users: Optional[list[GcpUser]] = Field(alias="users",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .gcp_identity import GcpIdentity
from .gcp_service_account import GcpServiceAccount
from .gcp_user import GcpUser

