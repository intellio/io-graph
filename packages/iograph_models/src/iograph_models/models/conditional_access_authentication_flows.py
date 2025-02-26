from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ConditionalAccessAuthenticationFlows(BaseModel):
	transferMethods: Optional[ConditionalAccessTransferMethods] = Field(default=None,alias="transferMethods",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .conditional_access_transfer_methods import ConditionalAccessTransferMethods

