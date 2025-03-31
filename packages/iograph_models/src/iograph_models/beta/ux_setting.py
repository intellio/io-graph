from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class UxSetting(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.uxSetting"] = Field(alias="@odata.type",)
	restrictNonAdminAccess: Optional[NonAdminSetting | str] = Field(alias="restrictNonAdminAccess", default=None,)

from .non_admin_setting import NonAdminSetting
