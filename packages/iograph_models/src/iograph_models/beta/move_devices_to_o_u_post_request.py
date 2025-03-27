from __future__ import annotations
from uuid import UUID
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Move_devices_to_o_uPostRequest(BaseModel):
	deviceIds: Optional[list[UUID]] = Field(alias="deviceIds", default=None,)
	organizationalUnitPath: Optional[str] = Field(alias="organizationalUnitPath", default=None,)


