from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UpdateAllMessagesReadStateOperationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[UpdateAllMessagesReadStateOperation]] = Field(alias="value", default=None,)

from .update_all_messages_read_state_operation import UpdateAllMessagesReadStateOperation
