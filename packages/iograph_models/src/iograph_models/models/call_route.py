from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CallRoute(BaseModel):
	final: Optional[IdentitySet] = Field(default=None,alias="final",)
	original: Optional[IdentitySet] = Field(default=None,alias="original",)
	routingType: Optional[RoutingType] = Field(default=None,alias="routingType",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .identity_set import IdentitySet
from .identity_set import IdentitySet
from .routing_type import RoutingType

