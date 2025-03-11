from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class EnablePostRequest(BaseModel):
	appOwnerTenantId: Optional[str] = Field(alias="appOwnerTenantId",default=None,)


