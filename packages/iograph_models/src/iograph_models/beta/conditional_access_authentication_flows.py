from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ConditionalAccessAuthenticationFlows(BaseModel):
	transferMethods: Optional[ConditionalAccessTransferMethods | str] = Field(alias="transferMethods", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .conditional_access_transfer_methods import ConditionalAccessTransferMethods
