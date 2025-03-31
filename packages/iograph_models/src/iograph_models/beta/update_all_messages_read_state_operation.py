from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class UpdateAllMessagesReadStateOperation(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.updateAllMessagesReadStateOperation"] = Field(alias="@odata.type",)
	resourceLocation: Optional[str] = Field(alias="resourceLocation", default=None,)
	status: Optional[MailFolderOperationStatus | str] = Field(alias="status", default=None,)

from .mail_folder_operation_status import MailFolderOperationStatus
