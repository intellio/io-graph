from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ArchivedPrintJob(BaseModel):
	acquiredByPrinter: Optional[bool] = Field(alias="acquiredByPrinter", default=None,)
	acquiredDateTime: Optional[datetime] = Field(alias="acquiredDateTime", default=None,)
	completionDateTime: Optional[datetime] = Field(alias="completionDateTime", default=None,)
	copiesPrinted: Optional[int] = Field(alias="copiesPrinted", default=None,)
	createdBy: Optional[UserIdentity] = Field(alias="createdBy", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	id: Optional[str] = Field(alias="id", default=None,)
	printerId: Optional[str] = Field(alias="printerId", default=None,)
	printerName: Optional[str] = Field(alias="printerName", default=None,)
	processingState: Optional[PrintJobProcessingState | str] = Field(alias="processingState", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .user_identity import UserIdentity
from .print_job_processing_state import PrintJobProcessingState

