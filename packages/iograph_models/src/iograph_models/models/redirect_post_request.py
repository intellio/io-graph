from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class RedirectPostRequest(BaseModel):
	destinationPrinterId: Optional[str] = Field(default=None,alias="destinationPrinterId",)
	configuration: Optional[PrintJobConfiguration] = Field(default=None,alias="configuration",)

from .print_job_configuration import PrintJobConfiguration

