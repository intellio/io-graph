from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CallRoute(BaseModel):
	final: SerializeAsAny[Optional[IdentitySet]] = Field(alias="final",default=None,)
	original: SerializeAsAny[Optional[IdentitySet]] = Field(alias="original",default=None,)
	routingType: Optional[RoutingType | str] = Field(alias="routingType",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .identity_set import IdentitySet
from .identity_set import IdentitySet
from .routing_type import RoutingType

