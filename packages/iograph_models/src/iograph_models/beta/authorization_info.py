from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AuthorizationInfo(BaseModel):
	certificateUserIds: Optional[list[str]] = Field(alias="certificateUserIds", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


