from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Acl(BaseModel):
	accessType: Optional[AccessType | str] = Field(alias="accessType", default=None,)
	identitySource: Optional[IdentitySourceType | str] = Field(alias="identitySource", default=None,)
	type: Optional[AclType | str] = Field(alias="type", default=None,)
	value: Optional[str] = Field(alias="value", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .access_type import AccessType
from .identity_source_type import IdentitySourceType
from .acl_type import AclType
