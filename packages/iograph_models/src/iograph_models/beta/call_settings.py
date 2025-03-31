from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class CallSettings(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.callSettings"] = Field(alias="@odata.type",)
	delegates: Optional[list[DelegationSettings]] = Field(alias="delegates", default=None,)
	delegators: Optional[list[DelegationSettings]] = Field(alias="delegators", default=None,)

from .delegation_settings import DelegationSettings
