from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Remove_from_drivePostRequest(BaseModel):
	driveId: Optional[str] = Field(alias="driveId",default=None,)


