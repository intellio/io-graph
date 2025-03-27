from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Mailbox(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.mailbox"] = Field(alias="@odata.type", default="#microsoft.graph.mailbox")
	deletedDateTime: Optional[datetime] = Field(alias="deletedDateTime", default=None,)
	folders: Optional[list[MailboxFolder]] = Field(alias="folders", default=None,)

from .mailbox_folder import MailboxFolder

