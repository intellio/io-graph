from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Add_appsPostRequest(BaseModel):
	productIds: Optional[list[str]] = Field(alias="productIds", default=None,)


