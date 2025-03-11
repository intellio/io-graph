from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Add_large_gallery_viewPostRequest(BaseModel):
	clientContext: Optional[str] = Field(alias="clientContext",default=None,)


