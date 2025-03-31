from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DelegatedAdminAccessContainer(BaseModel):
	accessContainerId: Optional[str] = Field(alias="accessContainerId", default=None,)
	accessContainerType: Optional[DelegatedAdminAccessContainerType | str] = Field(alias="accessContainerType", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .delegated_admin_access_container_type import DelegatedAdminAccessContainerType
