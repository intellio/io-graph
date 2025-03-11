from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UpdateAllMessagesReadStateOperation(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	resourceLocation: Optional[str] = Field(alias="resourceLocation",default=None,)
	status: Optional[MailFolderOperationStatus | str] = Field(alias="status",default=None,)

from .mail_folder_operation_status import MailFolderOperationStatus

