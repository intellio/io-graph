from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ArchivedPrintJob(BaseModel):
	acquiredByPrinter: Optional[bool] = Field(default=None,alias="acquiredByPrinter",)
	acquiredDateTime: Optional[datetime] = Field(default=None,alias="acquiredDateTime",)
	completionDateTime: Optional[datetime] = Field(default=None,alias="completionDateTime",)
	copiesPrinted: Optional[int] = Field(default=None,alias="copiesPrinted",)
	createdBy: Optional[UserIdentity] = Field(default=None,alias="createdBy",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	id: Optional[str] = Field(default=None,alias="id",)
	printerId: Optional[str] = Field(default=None,alias="printerId",)
	printerName: Optional[str] = Field(default=None,alias="printerName",)
	processingState: Optional[PrintJobProcessingState] = Field(default=None,alias="processingState",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .user_identity import UserIdentity
from .print_job_processing_state import PrintJobProcessingState

