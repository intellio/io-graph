from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RedirectPostRequest(BaseModel):
	destinationPrinterId: Optional[str] = Field(alias="destinationPrinterId",default=None,)
	configuration: Optional[PrintJobConfiguration] = Field(alias="configuration",default=None,)

from .print_job_configuration import PrintJobConfiguration

