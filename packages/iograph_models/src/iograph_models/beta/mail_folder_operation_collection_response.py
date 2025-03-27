from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class MailFolderOperationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[UpdateAllMessagesReadStateOperation],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .update_all_messages_read_state_operation import UpdateAllMessagesReadStateOperation

