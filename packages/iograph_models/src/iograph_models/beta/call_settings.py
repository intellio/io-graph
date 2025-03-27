from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CallSettings(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	delegates: Optional[list[DelegationSettings]] = Field(alias="delegates", default=None,)
	delegators: Optional[list[DelegationSettings]] = Field(alias="delegators", default=None,)

from .delegation_settings import DelegationSettings
from .delegation_settings import DelegationSettings

