from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DefaultSharingLink(BaseModel):
	defaultToExistingAccess: Optional[bool] = Field(alias="defaultToExistingAccess",default=None,)
	role: Optional[SharingRole | str] = Field(alias="role",default=None,)
	scope: Optional[SharingScope | str] = Field(alias="scope",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .sharing_role import SharingRole
from .sharing_scope import SharingScope

