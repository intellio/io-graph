from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class HyperlinkPostRequest(BaseModel):
	linkLocation: Optional[str] = Field(alias="linkLocation",default=None,)
	friendlyName: Optional[str] = Field(alias="friendlyName",default=None,)


