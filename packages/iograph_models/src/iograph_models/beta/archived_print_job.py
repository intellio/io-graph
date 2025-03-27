from __future__ import annotations
from typing import Optional
from typing import Union
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ArchivedPrintJob(BaseModel):
	acquiredByPrinter: Optional[bool] = Field(alias="acquiredByPrinter", default=None,)
	acquiredDateTime: Optional[datetime] = Field(alias="acquiredDateTime", default=None,)
	blackAndWhitePageCount: Optional[int] = Field(alias="blackAndWhitePageCount", default=None,)
	colorPageCount: Optional[int] = Field(alias="colorPageCount", default=None,)
	completionDateTime: Optional[datetime] = Field(alias="completionDateTime", default=None,)
	copiesPrinted: Optional[int] = Field(alias="copiesPrinted", default=None,)
	createdBy: Optional[Union[AuditUserIdentity]] = Field(alias="createdBy", default=None,discriminator="odata_type", )
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	duplexPageCount: Optional[int] = Field(alias="duplexPageCount", default=None,)
	id: Optional[str] = Field(alias="id", default=None,)
	pageCount: Optional[int] = Field(alias="pageCount", default=None,)
	printerId: Optional[str] = Field(alias="printerId", default=None,)
	printerName: Optional[str] = Field(alias="printerName", default=None,)
	processingState: Optional[PrintJobProcessingState | str] = Field(alias="processingState", default=None,)
	simplexPageCount: Optional[int] = Field(alias="simplexPageCount", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .audit_user_identity import AuditUserIdentity
from .print_job_processing_state import PrintJobProcessingState

