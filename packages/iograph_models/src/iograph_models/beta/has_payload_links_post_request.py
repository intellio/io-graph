from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Has_payload_linksPostRequest(BaseModel):
	payloadIds: Optional[list[str]] = Field(alias="payloadIds",default=None,)


