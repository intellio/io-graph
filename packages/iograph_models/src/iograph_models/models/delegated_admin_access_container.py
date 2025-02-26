from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DelegatedAdminAccessContainer(BaseModel):
	accessContainerId: Optional[str] = Field(default=None,alias="accessContainerId",)
	accessContainerType: Optional[DelegatedAdminAccessContainerType] = Field(default=None,alias="accessContainerType",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .delegated_admin_access_container_type import DelegatedAdminAccessContainerType

