from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UxSetting(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	restrictNonAdminAccess: Optional[NonAdminSetting | str] = Field(alias="restrictNonAdminAccess",default=None,)

from .non_admin_setting import NonAdminSetting

