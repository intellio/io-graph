from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RetryPostRequest(BaseModel):
	cloudPcIds: Optional[list[str]] = Field(alias="cloudPcIds",default=None,)


