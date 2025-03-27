from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Update_all_messages_read_statePostRequest(BaseModel):
	isRead: Optional[bool] = Field(alias="isRead", default=None,)
	suppressReadReceipts: Optional[bool] = Field(alias="suppressReadReceipts", default=None,)


