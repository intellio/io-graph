from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Download_powerlift_app_diagnosticPostRequest(BaseModel):
	request: Optional[PowerliftAppDiagnosticDownloadRequest] = Field(alias="request", default=None,)

from .powerlift_app_diagnostic_download_request import PowerliftAppDiagnosticDownloadRequest
