from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Create_server_log_collection_requestPostRequest(BaseModel):
	startDateTime: Optional[datetime] = Field(alias="startDateTime",default=None,)
	endDateTime: Optional[datetime] = Field(alias="endDateTime",default=None,)


